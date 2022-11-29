#Task :
    
"""
3. A very common use of broadcasting is to standardize data, i.e., to make it have zero
   mean and unit variance.
   a. First, create a fake “data set” with 50 examples, each with five dimensions.
   b. import numpy.random as npr
      data = np.exp ( npr.randn(50, 5) )
   c. Don’t worry too much about what this code is doing at this stage of the
      course, but for completeness: it imports the NumPy random number
      generation library, then generates a 50 × 5 matrix of standard normal random
      variates and exponentiates them. The effect of this is to have a pretend data
      set of 50 independent and identically-distributed vectors from a log-normal
      distribution.
4. Now, compute the mean and standard deviation of each column. This should result in
   two vectors of length 5. You’ll need to think a little bit about how to use the axis
   argument to mean and std. Store these vectors into variables and print both of them.
5. Now standardize the data matrix by 1) subtracting the mean off of each column, and
   2) dividing each column by its standard deviation. Do this via broadcasting, and store
   the result in a matrix called normalized. To verify that you successfully did it, compute
   the mean and standard deviation of the columns of normalized and print them out.

"""

#Program :



import numpy as np
import numpy.random as npr
from sklearn.preprocessing import MinMaxScaler
from warnings import simplefilter


def Mean_StandardDeviation():
    data = np.exp ( npr.randn(50, 5) )
    
    ArrayValues  = np.array( data )
    LengthOfData = len( ArrayValues )
    ShpaeValue   = np.shape( ArrayValues )
    ColumnValue  = ShpaeValue[1]
    
    mean_list=[]
    Standard_Deviation=[]
    for col in np.arange( ColumnValue ):
        ListOfValues =  []
        for row in np.arange( LengthOfData ):   
                val  =  ArrayValues[ row, col ]
                ListOfValues.append( val )
                
        column_vise_values = np.array( ListOfValues )
        Mean_Value         = np.mean( column_vise_values )
        Standard_Dev       = np.std( column_vise_values )
        
        # print( Mean_Value, Standard_Dev )  
        mean_list.append( Mean_Value )
        Standard_Deviation.append( Standard_Dev )
        
    MeanOfColumns=np.array( mean_list )
    StandardDeviationOfColumns=np.array( Standard_Deviation )    
    print( "\t\tMean\t:",MeanOfColumns,"\nStandard Deviation :",StandardDeviationOfColumns ) 
    
    SubOfColumnsByMean  = MeanOfColumns - ArrayValues
    
    Normalized         = np.matrix( SubOfColumnsByMean /  StandardDeviationOfColumns )


    scaler = MinMaxScaler()
    scaler.fit(Normalized)
    scaler.data_max_
    print('\n******************************* Normalized *******************************\n',scaler.transform(Normalized))

simplefilter(action='ignore', category=FutureWarning)

Mean_StandardDeviation()

 

