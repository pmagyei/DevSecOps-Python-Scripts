feed_alpha = ['10.0.0.5', '192.168.1.50', '172.16.0.8', '10.0.0.5']
feed_beta = ['172.16.0.8', '203.0.113.42', '192.168.1.50', '198.51.100.23']


# merging lists while keeping the original intact, creating a new list

combined_list = feed_alpha + feed_beta
feed_master = set(combined_list)
print(feed_master) #set() removes duplicates from a sequence


# extend the lists; however, one of the lists is mutated

feed_alpha.extend(feed_beta)

print(set(feed_alpha))