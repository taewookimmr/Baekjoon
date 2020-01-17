import java.util.*

fun main(args: Array<String>)=with(Scanner(System.`in`)){
    val nk = nextLine()
    val nums = nk.split(" ").map{it.toInt()}
    val n = nums[0]
    val k = nums[1]

    val lst : MutableList<String> = mutableListOf()
    for (i in 1..n){
        lst.add(nextLine())
    }

    for (e in lst){
        println(e)
    }
}