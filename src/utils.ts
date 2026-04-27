export function roll() : number {
    return Math.floor(Math.random() * 6) + 1;
}

export type Player = "p1" | "p2" ;

export type GameState = {
    p1_total : number;
    p2_total : number;
    current_player: Player;
    current_message: string;
}

