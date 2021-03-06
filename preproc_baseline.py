import numpy as np

def covariance_matrx(data):
    n_regions = 48
    A = np.zeros((n_regions, n_regions))
    for i in range(n_regions):
        for j in range(i, n_regions):
            if i == j:
                A[i][j] = 1
            else:
                A[i][j] = abs(np.corrcoef(data[i, :], data[j, :])[0][1])  # get value from corrcoef matrix
                A[j][i] = A[i][j]
    upper_tri_flattened = A[np.triu_indices(48, k=0)]
    #print(upper_tri_flattened)
    return upper_tri_flattened

def gaussian_matrix(data, sigma = 1):
    n_regions = 48
    A = np.zeros((n_regions, n_regions))
    for i in range(n_regions):
        for j in range(i, n_regions):
            dist = np.linalg.norm(data[i, :] - data[j, :])
            A[i][j] = np.exp(-dist**2/(2.*(sigma**2.)))
            A[j][i] = A[i][j]
    upper_tri_flattened = A[np.triu_indices(48, k=0)]
    #print(upper_tri_flattened)
    return upper_tri_flattened

if __name__ == '__main__':
    train_data = np.load('/scratch/bigdata/ABCD/abcd-fmriprep-rs/ST-GCN-data/harvardoxford/harvardoxford_train_data_1.npy').squeeze()
    test_data = np.load('/scratch/bigdata/ABCD/abcd-fmriprep-rs/ST-GCN-data/harvardoxford/harvardoxford_test_data_1.npy').squeeze()
    train_label = np.load('/scratch/bigdata/ABCD/abcd-fmriprep-rs/ST-GCN-data/harvardoxford/harvardoxford_train_label_1.npy')
    test_label = np.load('/scratch/bigdata/ABCD/abcd-fmriprep-rs/ST-GCN-data/harvardoxford/harvardoxford_test_label_1.npy')


    # abs of covariance matrix
    train_data_covar = np.zeros((train_data.shape[0], 1176))
    test_data_covar = np.zeros((test_data.shape[0], 1176))
    for i in range(train_data.shape[0]):
        train_data_covar[i] = covariance_matrx(train_data[i].T)
        i += 1
    for i in range(test_data.shape[0]):
        test_data_covar[i] = covariance_matrx(test_data[i].T)
        i += 1
    np.save('./data/train_data_baseline_1_abs.npy', train_data_covar)
    np.save('./data/test_data_baseline_1_abs.npy', test_data_covar)
0
    # gaussian kernel
    # train_data_gaussian = np.zeros((train_data.shape[0], 1176))  # batch *
    # test_data_gaussian = np.zeros((test_data.shape[0], 1176))
    #
    # for i in range(train_data.shape[0]):
    #     train_data_gaussian[i] = gaussian_matrix(train_data[i].T)
    #     i += 1
    # for i in range(test_data.shape[0]):
    #     test_data_gaussian[i] = gaussian_matrix(test_data[i].T)
    #     i += 1
    #
    # np.save('./data/train_data_baseline_1_gaussian.npy', train_data_gaussian)
    # np.save('./data/test_data_baseline_1_gaussian.npy', test_data_gaussian)



