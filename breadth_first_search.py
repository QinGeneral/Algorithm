from collections import deque


def is_mogo_seller(name):
    if 'm' in name:
        return True
    else:
        return False


# 广度优先搜索算法
def main():
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = ["asdf"]
    graph["asdf"] = ["anuj"]
    graph["peggy"] = ["mmmm"]
    graph["mmmm"] = ["peggy"]
    graph["thom"] = []
    graph["jonny"] = []
    checked_list = []

    search_queue = deque()
    search_queue += graph["you"]
    while search_queue:
        people = search_queue.popleft()

        is_in_checked_list = people in checked_list
        print("is in checked list " + str(is_in_checked_list))
        if (not is_in_checked_list) and is_mogo_seller(people):
            print("find it: " + people)
        else:
            if not is_in_checked_list:
                print("not find: " + people)
                search_queue += graph[people]
            else:
                print("is in")

        checked_list.append(people)


main()
