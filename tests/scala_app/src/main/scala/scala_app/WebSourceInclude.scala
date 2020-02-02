package scala_app


// @@@ BEGIN: https://raw.githubusercontent.com/mrange/WebSourceInclude/master/tests/scala_include/streams/PushStream.scala

package web_source_include.streams {

// ### INCLUDE: ../logs/Log.scala
// @@@ INCLUDE: https://raw.githubusercontent.com/mrange/WebSourceInclude/master/tests/scala_include/logs/Log.scala

trait PushStream[+T] {
  def build(r: T => Boolean): Boolean
}

object PushStream {
  def empty = new PushStream[Nothing] {
    def build(r: Nothing => Boolean): Boolean = true
  }
}

}
// @@@ END: https://raw.githubusercontent.com/mrange/WebSourceInclude/master/tests/scala_include/streams/PushStream.scala


// @@@ BEGIN: https://raw.githubusercontent.com/mrange/WebSourceInclude/master/tests/scala_include/logs/Log.scala

package web_source_include.logs {

trait Log {
  def log(m: String): Unit
}

}

// @@@ END: https://raw.githubusercontent.com/mrange/WebSourceInclude/master/tests/scala_include/logs/Log.scala


// @@@ SKIPPED (already seen): https://raw.githubusercontent.com/mrange/WebSourceInclude/master/tests/scala_include/logs/Log.scala
