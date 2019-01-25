open System
open System.Text

[<EntryPoint>]
let main argv =
    let numCases = Console.ReadLine() |> int
    for i = numCases downto 1 do
        let strIn = Console.ReadLine()
        let pairs = Seq.pairwise strIn
        let ignoredTupleValue = ('1', '1')
        let swappedTuples = pairs |> Seq.mapi (fun idx pair ->
                                if idx % 2 = 0 then
                                    let (a, b) = pair
                                    (b, a)
                                else
                                    ignoredTupleValue)
        let answer = Seq.fold (fun (sb : StringBuilder) pair ->
                                if pair <> ignoredTupleValue then
                                    let (a, b) = pair
                                    sb.Append(a) |> ignore
                                    sb.Append(b) |> ignore
                                sb)
                                (new StringBuilder())
                                swappedTuples
        printfn "%s" (answer.ToString())
