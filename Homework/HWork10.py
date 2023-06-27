# | Задание 44 |
# | --- |
# | В ячейке ниже представлен код генерирующий DataFrame, которая 
# состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. 
# Сможете ли вы это сделать без get_dummies?


# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data.head() |

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data)

one_hot = pd.get_dummies(data['whoAmI'])

one_hot_sum = one_hot.sum(axis=1)

data = pd.concat([data, one_hot], axis=1)

print(data)
