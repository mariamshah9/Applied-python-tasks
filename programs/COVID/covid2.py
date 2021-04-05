import json


output_file_handle = open("newcovid.csv","w") 
row="condition,condition_cui,label,label_cui,label_score,label_semantic_types,label_ncts,label_bucket,label_ncts_counts"
output_file_handle.write(row+"\n")



with open('covid-19.json','r') as json_file:
    data = json.load(json_file)		
    for condition_k, condition_value in data.items():
        print("condition"+condition_k)
        condition=condition_k
        for condition_sub_key, condition_sub_value in condition_value.items():
            if(condition_sub_key=='cui') :
                print( "condition_cui"+str(condition_sub_value))
                condition_cui=str(condition_sub_value)
            else:
                print( "label_bucket"+str(condition_sub_key))
                label_bucket=str(condition_sub_key)
                for label,labelcui_k in condition_sub_value.items():
                    print( "label="+str(label))
                    for other_k, other_v in labelcui_k.items():
                        if(other_k=='cui'):
                            print("label_cui="+str(other_v))
                            label_cui=str(other_v)
                        elif(other_k=='score'):
                            print("label_score="+str(other_v))
                            label_score=str(other_v) 
                        elif(other_k=='label_semantic_types'):
                            print("label_semantic_types="+str(other_v))
                            label_semantic_types=str(other_v)
                        elif(other_k=='ncts'):
                            print("label_ncts="+str(other_v))
                            label_ncts=str(other_v)
                        elif(other_k=='label_ncts_counts'):
                            print("label_ncts_counts="+str(other_v))
                            label_ncts_counts=str(other_v)
                            
                    row=condition+','+condition_cui+','+label+',"'+label_cui+'",'+label_score+','+label_semantic_types+',"'+label_ncts+'",'+label_bucket+','+label_ncts_counts
                    print(row)
                    output_file_handle.write(row+"\n")
                    
                    
                    
output_file_handle.close()