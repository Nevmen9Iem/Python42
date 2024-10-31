##text = {"Movie","Game","App","Play",5,8,10,11,21,47,"Mobile","Phone"}
##num_list = list(filter(lambda i: i if str(i).isdigit()==True else False, text))
##num_list = set(num_list)
##print("Set num >", num_list)
##text_list = list(filter(lambda i: i if str(i).isalpha() == True else False, text))
##text_list = set(text_list)
##print("Set Word >", text_list)
##print("\n\n\n")
##
##import random
##
##random_list = [random.randint(1,50) for i in range(20)]
##set_list = set(random_list)
##print("Random list >", set_list)
##print("Set_num >", num_list)
##
##set1 = num_list & set_list
##print("Set1 >", set1)
##set2 = num_list | set_list
##print("Set2 >", set2)
##set3 = num_list - set_list
##print("Set3 >", set3)
##set4 = set_list.symmetric_difference(num_list)
##print("Set4 >", set4)
##print("Set1 max =", max(set1), "Set1 min =", min(set1)) 
##print("Set2 max =", max(set2), "Set2 min =", min(set2))
##print("Set3 max =", max(set3), "Set3 min =", min(set3), "Sorted set3 >", sorted(set3))
##set4_rev = sorted(set4, reverse = True)
##print("Set4_rev =", set4_rev)
##
##set4_list = [str(set4_rev[i]) for (i) in range(len(set4_rev))]
##print("".join(set4_list))

[[1,2,3],[1,2,3],[1,2,3]]
