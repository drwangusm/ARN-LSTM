import csv
import sys

AVG_BASED_ON_ACTUAL = True #根据实际结果或预测结果计算平均值

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Usage: " + sys.argv[0] + " [attention.csv file]")
        exit(0)
    else:
        model = sys.argv[1]
   
    print("")
    print ("Model: " + model.split('/')[3])

    att_vec_avg = {}
    samples_count = {}

    with open(sys.argv[1]) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for idx, row in enumerate(reader):
            if idx != 0:  # Skip header
                actual = row.pop(0)
                predicted = row.pop(0)
                
                if AVG_BASED_ON_ACTUAL:
                    index = actual
                else:
                    index = predicted
                
                if index in att_vec_avg:  #Means also in sample count
                    samples_count[index] += 1
                    print(row)
                    att_vec_avg[index] = [(float(x) + float(y)) for (x,y) in zip(att_vec_avg[index], row)] # Sum element wise in list
                    
                else:
                    att_vec_avg[index] = row
                    samples_count[index] = 1
        
        for index in samples_count:
            att_vec_avg[index] = [float(x) / samples_count[index] for x in att_vec_avg[index]]  # Compute average
            print ("Data Class:", index)
            print ("Attention Vector:", att_vec_avg[index])            
        

                

