import os

test_folder = 'tf_files/testingimages/'

test_file_list = [f for f in os.listdir(test_folder) if f != '.DS_Store']
test_file_list.sort()

for test_file in test_file_list:
    os.system('python3 -m scripts.label_image --graph=tf_files/retrained_graph.pb --image={}'.format(test_folder+test_file))
    print('result for {}'.format(test_file))
    print('\n')


