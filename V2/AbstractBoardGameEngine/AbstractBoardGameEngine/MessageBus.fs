namespace ABGE
#nowarn "40"

module Messages = 

    type Message (content, saga_id) =
        member this.content = content
        member this.saga_id = saga_id
        static member CreateMessage(content, saga_id) = 
            Message(content, saga_id)

    type MessageHandler = Message -> Unit

    let print_message (message:Message) = printfn "%s" message.content
    let print_message_again (message:Message) = printfn "%s" message.content

    let MB2 process_message = 
        MailboxProcessor.Start(fun inbox ->

            let rec loop = async {
                let! msg = inbox.Receive()
                process_message msg
                return! loop
                }
            loop)
    
    type MessageBusFactory (handlers:list<MessageHandler>) = 
        
        member this.handlers = handlers
        member this.add_handler (handler:MessageHandler) = 
            new MessageBusFactory(List.append this.handlers [handler])
        member this.create_message_bus = 
            let processing_function (handlers:list<MessageHandler>) (message:Message) = 
                handlers |> List.iter(fun handler -> handler message)
            MB2 (processing_function handlers)