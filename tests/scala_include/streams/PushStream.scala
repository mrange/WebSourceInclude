package web_source_include.streams

// ### INCLUDE: ../logs/Log.scala

trait PushStream[+T] {
  def build(r: T => Boolean): Boolean
}

object PushStream {
  def empty = new PushStream[Nothing] {
    def build(r: T => Boolean): Boolean = true
  }
}