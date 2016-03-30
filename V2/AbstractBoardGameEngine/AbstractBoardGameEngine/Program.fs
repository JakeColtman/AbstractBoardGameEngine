

[<EntryPoint>]
let main argv = 
    let handlers = [ABGE.Messages.print_message; ABGE.Messages.print_message_again]
    let bus = ABGE.Messages.create_message_bus handlers
    bus.Post "Hello"
    System.Console.Read() |> ignore
    0 // return an integer exit code
