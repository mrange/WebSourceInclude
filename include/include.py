import urllib.request
import re


root_url      = "https://raw.githubusercontent.com/mrange/WebSourceInclude/master/tests/scala_include/"
target_file   = "../tests/scala_app/src/main/scala/scala_app/WebSourceInclude.scala"
root_package  = "scala_app"

class Include:
  def __init__(self, path):
    self.path = path

  def uri(self):
    return root_url + self.path


includes = [
    Include("streams/PushStream.scala")
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

  if current:
    for include in current:
      uri = include.uri()

      if uri in seen:
        print("Skipping (already seen): %s" % uri)
        lines.append("")
        lines.append("// @@@ SKIPPED (already seen): %s" % uri)
        lines.append("")
      else:
        seen.add(uri)
        print("Downloading: %s" % uri)
        lines.append("")
        lines.append("// @@@ BEGIN: %s" % uri)
        lines.append("")

        with urllib.request.urlopen(uri) as response:
          content = response.read().decode("utf-8")
          for line in content.splitlines():
            lines.append(line)

        lines.append("")
        lines.append("// @@@ END: %s" % uri)
        lines.append("")
    current = nxt
    nxt = []

  total = "\n".join(lines)

  with open(target_file,"w") as target:
    target.write(total)

generate_target_file()