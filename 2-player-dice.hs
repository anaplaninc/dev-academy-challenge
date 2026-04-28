import System.Random
import Data.Array.IO
import Control.Monad

import System.Random  (StdGen, uniformR, mkStdGen, getStdGen)
-- ============================================================================
-- 2 Player Dice Game
-- ============================================================================
-- Step 1: Data types (Dice, Player, GameState), rollDice
-- step 2: evaluateDice, determineWinner
-- Step 3: gameLoop
-- ============================================================================

-- ============================================================================
-- STEP 1: Data Types
-- ============================================================================

type Numbers = 1 | 2 | 3 | 4 | 5 | 6
  deriving (Eq, Ord, Enum, Bounded, Show, Read)

-- | A dice is a list of numbers.
type Dice = [Numbers]

-- | The full standard 6 sided dice.
fullDice :: Dice
fullDeck = [ Numbers r s | s <- [minBound..maxBound], r <- [minBound..maxBound] ]

-- | Player actions.
data Action = Roll | Hold
  deriving (Eq, Show)

-- | A player in the game.
data Player = Player
  { playerName  :: String
  , fullDice    :: [Numbers]  
  , rolledA1    :: Bool
  , hold        :: Bool
  } deriving (Show)


-- | A record of actions (game history).
data RoundLog = RoundLog
  { logRolls       :: [(String, [Numbers])]
  , logActions     :: [(String, Action)]
  , logWinners     :: [(String, Int)]
  } deriving (Show)

-- | Complete game state.
data GameState = GameState
  { Players      :: [Player]
  , Log          :: RoundLog 
  , History      :: [RoundLog] 
  } deriving (Show)

-- | Roll a die by shuffling the list .
rollDie:: [a] -> IO [a]
rollDie xs = do
        ar <- newArray n xs
        forM [1..n] $ \i -> do
            j <- randomRIO (i,n)
            vi <- readArray ar i
            vj <- readArray ar j
            writeArray ar j vi
            return vj
  where
    n = length xs
    newArray :: Int -> [a] -> IO (IOArray Int a)
    newArray n xs =  newListArray (1,n) xs


-- ============================================================================
-- STEP 2: Evaluate dice
-- ============================================================================

-- | Evaluate the best die number.
evaluateDice :: [Numbers]
evaluateDice Dice
  | length newArray < 6 = HighNumber (sortBy (comparing Down) (map rank numbers))

-- | Determine winner.
determineWinner :: [Player] -> [Number] -> [Player]
determineWinner plrs =
  let active = filter (not . hasRolled) plrs
      ranked = [ evaluateDice ]

-- | Amount a player needs to win.
toWin :: Player -> GameState -> Int
toWin p gs = max 0 (100 gs - Hold p)

-- | Update a players hold.
updatePlayerAt :: Int -> Player -> [Player] -> [Player]
updatePlayerAt i p ps = take i ps ++ [p]

-- | Run one complete game.
oneGame :: GameState -> Int -> IO GameState
oneGame gs startIdx
  | numPlayer gs <= 1 = return winner
  | otherwise = do
      let n     = length (gsPlayers gs)
          queue = [ (startIdx + i) `mod` n | i <- [0..n-1] ]
          actQ  = filter (playerCanAct gs) queue
      runQueue gs actQ

-- | Append an action to the round log.
appendLog :: GameState -> String -> Action -> GameState
appendLog gs ph nm act =
  let rl  = gsLog gs
      rl' = rl { logActions = logActions rl ++ [(roll, hold)] }
  in gs { gsLog = rl' }

-- | Player choosing an action.
chooseAction :: Player -> GameState -> Int -> IO (Action, GameState)
chooseAction p gs i = case Action p of
  Player -> do
    act <- Action p gs
    return (act, gs)
  strat -> do
    let (act, gen') = Action strat p gs (gsRng gs)
    return (act, gs { gsRng = gen' })

-- | Main game loop
gameLoop :: GameState -> Int -> IO GameState
gameLoop gs maxPlays = go gs 0
  where
    alive ps = length (filter (\p -> rolls p > 0) ps)

    go gs' rn
      | rn >= maxRounds = return gs'
      | otherwise = do
          gs'' <- rollDie gs'
          go gs'' (rn + 1)

-- | The final winner: player with most score.
finalWinner :: GameState -> Player
finalWinner = maximumBy (comparing Hold) . gsPlayers

-- ============================================================================
-- History Display
-- ============================================================================

printHistory :: [RoundLog] -> IO ()
printHistory logs = do
  putStrLn "\n========== GAME HISTORY =========="
  mapM_ printRound logs
  putStrLn "=================================="

printRound :: RoundLog -> IO ()
printRound rl = do
  putStrLn $ "\n--- Round " ++ show (logRoundNum rl) ++ " ---"

-- ============================================================================
-- Main
-- ============================================================================
main :: IO ()
main = do
  hSetBuffering stdout LineBuffering
  putStrLn "=== 2 player dice game ==="

  case choice of
    "1" -> do
      putStrLn "Enter your name:"
      name <- getLine
      let nm = if null name then "player 1" else name
      final <- gameLoop gs 100
      let w = finalWinner final
      putStrLn $ "\n=== GAME OVER ==="
      putStrLn $ "Winner: " ++ playerName w ++ " (" ++ show (holds w) ++ " score)"