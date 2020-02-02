package logs

trait Log {
  def log(m: String): Unit
}