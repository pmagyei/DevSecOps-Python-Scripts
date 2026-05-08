feed_alpha = ['10.0.0.5', '192.168.1.50', '172.16.0.8', '10.0.0.5']
feed_beta = ['172.16.0.8', '203.0.113.42', '192.168.1.50', '198.51.100.23']


# merging lists while keeping the original intact, creating a new list

combined_list = feed_alpha + feed_beta #adds the two lists together to create a new list
feed_master = list(set(combined_list)) #set() removes duplicates from a sequence. The stripped list is assigned to a new variable
print(feed_master)


# extend the lists; however, one of the lists is mutated
feed_alpha.extend(feed_beta) #adds the elements of feed_beat to the end of feed_alpha

print(set(feed_alpha))