import numpy as np

class AHP:
    def __init__(self,goal):
        self.goal=goal

    def make_matrix(self,count,name):
        criteria=[]
        for i in range(1,count+1):      # A for loop for criterias entries 
            criteria.append(str(input("{} {}:".format(name,i))))

        return criteria

    def make_criteria_matrix(self,criteria,alternative,text):
        critera_matrix = np.ones(shape=(len(criteria), len(criteria)))
        for i in range(len(alternative)):          # A for loop for row entries 
            for j in range(i,len(criteria)):      # A for loop for column entries
                if(i==j):
                    critera_matrix[i,j]=1
                else:
                    critera_matrix[i,j]=float(input("{} {} to {} ".format(text,criteria[i],criteria[j]))) 
                    critera_matrix[j,i]=1/critera_matrix[i,j]
        return critera_matrix

    def make_alternative_matrix(self,criteria,alternative,text):
        critera_matrix = np.ones(shape=(len(alternative), len(criteria)))
        for i in range(len(alternative)):          # A for loop for row entries 
            for j in range(len(criteria)):
                critera_matrix[i,j]=float(input("{} {} to {} ".format(text,alternative[i],criteria[j]))) 
        return critera_matrix

    def Calculate_Pairwise(self,matrix):
        matrix = matrix / matrix.sum(axis=0)
        weights_matrix = matrix.sum(axis=1)
        weights_matrix = weights_matrix/weights_matrix.sum(axis=0)
        return weights_matrix

    #find consistency of matrix
    def Calculate_Concistecy(self,matrix):
        weight_matreix=self.Calculate_Pairwise(matrix)
        multiply_matrix=(matrix.dot(weight_matreix.reshape(len(matrix), 1)))/weight_matreix.reshape(len(matrix), 1)
        print("multiply_matrix is"+str(multiply_matrix))
        CI=float(multiply_matrix.max())
        RI=[0,0,0.58,0.9,1.12,1.24,1.32,1.41,1.45,1.49]
        consistency=(CI-len(matrix))/(len(matrix)-1)
        if(consistency/RI[len(matrix)]<0.1):
            return "CI/RI < 0.1 is {} and consistent".format(consistency/RI[len(matrix)])
        return "CI/RI > 0.1 is {} and consistent".format(consistency/RI[len(matrix)])

    def Calculate_alternative_all_criteria(Self,alt_cri_matrix,criterias_weight,arternative_count):
        ranking=alt_cri_matrix*criterias_weight.reshape(arternative_count, 1)
        return ranking




if __name__ == "__main__":
    goal=str(input("The Goal is : "))
    ahp = AHP(goal)
    criteria_count=int(input("Criteria count is : "))
    list_of_criteria=ahp.make_matrix(criteria_count,"criteria")
    matrix_criteria=ahp.make_criteria_matrix(list_of_criteria,list_of_criteria,"Relative important ")


    print("------------------------------------------")
    
    print(ahp.Calculate_Concistecy(matrix_criteria))

    print("------------------------------------------")

    alternative_count=int(input("Alternative count is : "))
    list_of_alternative=ahp.make_matrix(alternative_count,"alternative")
    matrix_criteria_alternative=ahp.make_alternative_matrix(list_of_criteria,list_of_alternative,"Relative Alternative vs Criteria ")

    print(matrix_criteria_alternative)

    
    criteria_matreix=ahp.Calculate_Pairwise(matrix_criteria)

    print(matrix_criteria_alternative.dot(criteria_matreix.reshape(criteria_count, 1)))


