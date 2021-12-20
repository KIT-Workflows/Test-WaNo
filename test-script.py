import matplotlib.pyplot as plt
import numpy as np
import yaml, sys


if __name__ == '__main__':

    with open('rendered_wano.yml') as file:
        wano_file = yaml.full_load(file)
    
    with open("output_dict.yml",'w') as out:
        yaml.dump(wano_file, out,default_flow_style=False)

    start = wano_file["simple-Dictbox"]["start"]
    stop = wano_file["simple-Dictbox"]["stop"]
    step = wano_file["simple-Dictbox"]["step"]


    if start < stop:
        print("correct inputs")
    else:
        print("Received error: var-0 can't be larger than var-1")
        sys.exit()

    x1 = np.arange(start, stop, step)
    
    fig = plt.figure(figsize=(16,9))	#identifies the figure 
    plt.title("Y vs X", fontsize='24')	#title
    plt.plot(x1, 0.1*x1**2, color='b',linewidth=4) #plot the points
    plt.xticks(fontsize=16) # Set XTick Labels Font Size 
    plt.yticks(fontsize=16) # Set YTick Labels Font Size 
    plt.xlabel("X",fontsize='20')	#adds a label in the x axis
    plt.ylabel("Y",fontsize='20')	#adds a label in the y axis
    plt.legend(('YvsX'),loc='best')	#creates a legend to identify the plot
    plt.grid() #shows a grid under the plot
    plt.savefig('figure.png')	#saves the figure in the present directory
    	
    