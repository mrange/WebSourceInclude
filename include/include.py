import re
import urllib.parse
import urllib.request

class UriInclude:
  def __init__(self, path):
    self.path = path

  def uri(self):
    return self.path

def include(path):
  return UriInclude(root_url + path)

root_url      = "https://raw.githubusercontent.com/mrange/WebSourceInclude/master/tests/scala_include/"
target_file   = "../tests/scala_app/src/main/scala/scala_app/WebSourceInclude.scala"
root_package  = "scala_app"

includes = [
    include("streams/PushStream.scala"),
    include("logs/Log.scala"),
  ]

regex_include = re.compile("""^\s*//\s*###\s*INCLUDE:\s*(?P<path>\S+)\s*$""")

def generate_target_file():
  seen = set()
  current = includes
  nxt = []
  lines = [
      "package %s" % root_package,
      ""
    ]

  while current:
    for include in current:
      uri = include.uri()

      print("Processing: %s" % uri)

      if uri in seen:
        print("  Skipping (already seen): %s" % uri)
        lines.append("")
        lines.append("// @@@ SKIPPED (already seen): %s" % uri)
        lines.append("")
      else:
        seen.add(uri)
        print("  Downloading: %s" % uri)
        lines.append("")
        lines.append("// @@@ BEGIN: %s" % uri)
        lines.append("")

        with urllib.request.urlopen(uri) as response:
          content = response.read().decode("utf-8")
          for line in content.splitlines():
            lines.append(line)
            m = regex_include.match(line)
            if m:
              path = m.group("path")
              inc = urllib.parse.urljoin(uri, path)
              print("  Found include: %s" % inc)
              lines.append("// @@@ INCLUDE: %s" % inc)
              nxt.append(UriInclude(inc))

        lines.append("")
        lines.append("// @@@ END: %s" % uri)
        lines.append("")
    current = nxt
    nxt = []

  total = "\n".join(lines)

  with open(target_file,"w") as target:
    target.write(total)

generate_target_file()