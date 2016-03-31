namespace ABGE

module TicTacToeDomain = 

    type HorizPosition = Left | HCenter | Right
    type VertPosition = Left | VCenter | Right

    type CellPosition = HorizPosition * VertPosition

    type Player = Player0 | PlayerX

    type PlayerXPos = PlayerXPos of CellPosition
    type PlayerYPos = PlayerYPos of CellPosition

    type CellState = 
        | Played of Player
        | Empty

    type Cell = {
        pos : CellPosition
        state: CellState
    }
        
    type GameState = {
        cells: Cell list
    }

    type GameStatus = 
        | InProgress
        | PlayerXWon
        | PlayerOWon
        | Draw

    type ValidMovesForPlayerX = PlayerXPos list
    type ValidMovesForPlayerO = PlayerYPos list

    type MoveResult = 
        | PlayerXToMove of GameState * ValidMovesForPlayerX
        | PlayerOToMove of GameState * ValidMovesForPlayerO
        | GameWon of GameState * Player
        | GameDrawn of GameState

    type PlayerXMoves = GameState * PlayerXPos -> 
                            GameState * MoveResult
    type PlayerOMoves = GameState * PlayerYPos -> 
                            GameState * MoveResult

    type GetCells = GameState -> Cell list

    type NewGame = GameState * MoveResult

