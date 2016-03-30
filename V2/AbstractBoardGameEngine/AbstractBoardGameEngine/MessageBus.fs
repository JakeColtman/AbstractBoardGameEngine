namespace ABGE
#nowarn "40"

module Messages = 
    type Issuer = 
        | User of username: string

    type Message = {Content: obj; SagaId: int; Issuer: Issuer}

    type MessageHandler = string -> Unit

    let print_message (message:string) = printfn "%s" message
    let print_message_again (message:string) = printfn "%s" message

    let MB2 process_message = 
        MailboxProcessor.Start(fun inbox ->

            let rec loop = async {
                let! msg = inbox.Receive()
                process_message msg
                return! loop
                }
            loop)

    let create_message_bus (handlers:list<MessageHandler>) = 
        let processing_function (handlers:list<MessageHandler>) (message:string) = 
            handlers |> List.iter(fun handler -> handler message)

        MB2 (processing_function handlers)