
# *******************
# v1.1
# *******************

def require_role_permission1(func):
  def wrapper(x):
    func(x+1)
  return wrapper


def func_target1(x):
  print(x)

# questo
func_target1 = require_role_permission1(func_target1)
func_target1(1)


# *******************
# v1.2
# *******************

def require_role_permission2(func):
  def wrapper(x):
    func(x+1)
  return wrapper

@require_role_permission2
def func_target2(x):
  print(x)

func_target2(1)



# ora io voglio passare un parametro a
# require_role_permission

# *******************
# v2.1
# *******************

def require_role_permission3(func):
  def outer(param):  
    def inner(x):
      if param == "aggiungi":
        func(x+1)
      elif param == "sottrai":
        func(x-1)
    return inner
  return outer

def func_target3(x):
  print(x)

# questo
func_target3 = require_role_permission3(func_target3)("aggiungi")
func_target3(1)


# *******************
# v2.2
# *******************


def require_role_permission4(func):
  def outer(param):  
    def inner(x):
      if param == "aggiungi":
        func(x+1)
      elif param == "sottrai":
        func(x-1)
    return inner
  return outer

@require_role_permission4("aggiungi")
def func_target4(x):
  print(x)

func_target4(1)


# *******************
# v3.1
# *******************


def require_role_permission5(param):
  def outer(func):  
    def inner(x):
      if param == "aggiungi":
        func(x+1)
      elif param == "sottrai":
        func(x-1)
    return inner
  return outer

def func_target5(x):
  print(x)

func_target5 = require_role_permission5("aggiungi")(func_target5)
func_target5(1)



# *******************
# v3.2
# *******************

def require_role_permission6(param):
  def outer(func):  
    def inner(x):
      if param == "aggiungi":
        func(x+1)
      elif param == "sottrai":
        func(x-1)
    return inner
  return outer


@require_role_permission6("aggiungi")
def func_target6(x):
  print(x)


func_target6(1)


