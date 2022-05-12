import numpy as np

def calculate(list):
    try:
        # Converting list into np.array 3x3
        imported_list = np.array(list)
        shape = (3,3)
        matrix = imported_list.reshape(shape)      
 
        # Mean
        axis1_mean = np.mean(matrix, axis=0).tolist()
        axis2_mean = np.mean(matrix, axis=1).tolist()
        flattened_mean = np.mean(matrix).tolist()
        mean_dic = [axis1_mean, axis2_mean, flattened_mean]
        
        # Variance
        axis1_var = np.var(matrix, axis=0).tolist()
        axis2_var = np.var(matrix, axis=1).tolist()
        flattened_var = np.var(matrix).tolist()
        var_dic = [axis1_var, axis2_var, flattened_var]
        
        # Standart Deviation
        axis1_std = np.std(matrix, axis=0).tolist()
        axis2_std = np.std(matrix, axis=1).tolist()
        flattened_std = np.std(matrix).tolist()
        std_dic = [axis1_std, axis2_std, flattened_std]
        
        # Max
        axis1_amax = np.amax(matrix, axis=0).tolist()
        axis2_amax = np.amax(matrix, axis=1).tolist()
        flattened_amax = np.amax(matrix).tolist()
        amax_dic = [axis1_amax, axis2_amax, flattened_amax]
        
        
        # Min
        axis1_amin = np.amin(matrix, axis=0).tolist()
        axis2_amin = np.amin(matrix, axis=1).tolist()
        flattened_amin = np.amin(matrix).tolist()
        amin_dic = [axis1_amin, axis2_amin, flattened_amin]
        
        # Sum
        axis1_sum = np.sum(matrix, axis=0).tolist()
        axis2_sum = np.sum(matrix, axis=1).tolist()
        flattened_sum = np.sum(matrix).tolist()
        sum_dic = [axis1_sum, axis2_sum, flattened_sum]

        # Create Dictionary
        calculations = {
                'mean': mean_dic,
                'variance': var_dic,
                'standard deviation': std_dic,
                'max': amax_dic,
                'min': amin_dic,
                'sum': sum_dic}
        
        return calculations
    
    except:
        raise ValueError ("List must contain nine numbers.")  