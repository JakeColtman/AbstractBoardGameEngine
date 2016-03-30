

[<EntryPoint>]
let main argv = 
    let handlers = [ABGE.Messages.print_message; ABGE.Messages.print_message_again]
    let factory = ABGE.Messages.MessageBusFactory handlers
    let bus = factory.create_message_bus
    bus.Post "Hello"
    let factory2 = factory.add_handler ABGE.Messages.print_message
    factory2.create_message_bus.Post "Hello 2"
    

    System.Console.Read() |> ignore
    0 // return an integer exit code
