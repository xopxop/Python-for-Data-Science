ft_list = ["Hello"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list.append("World!")

ft_tuple_list: list[str] = list(ft_tuple)
ft_tuple_list[1] = "Finland"
ft_tuple = tuple(ft_tuple_list)

ft_set.remove("tutu!")
ft_set.add("Helsinki")

ft_dict["Hello"] = "Hive Helsinki"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
