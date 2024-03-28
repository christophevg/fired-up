from fired_up import FiredUp, Menu, Group

class Commands(Group):
  def run(self):
    print("Commands> running...")

class SubCommands(Group):
  def run(self):
    print("SubCommands> running...")

class SubSubCommands(Group):
  def run(self):
    print("SubSubCommands> running...")

FiredUp(
  commands=Commands,
  submenu=Menu(
    commands=SubCommands,
    subsubmenu=Menu(
      commands=SubSubCommands
    )
  )
)
