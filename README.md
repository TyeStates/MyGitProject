# MyGitProject

Running this program will start with the user entering the weights of their marking scheme. IF there are not grades assigned to a type of item, they should enter 0. If something is weighted at 0,
it is ignored when the program actually goes through the weight array. It will clarify with the user if the weights are correct after entry, showing the user and asking if the user finds those to be 
accurate. The only way to say "No" is to type 0. Any other value is equivalent to saying "yes". If the user enters a "no" response, the system re-does the entry for weights. 

It then iterates through the non-zero weights and takes a user input of how many instances of each item type have been completed. Immediately after the input of the amount of the type of mark,
the system will take the actual grade from the user as a floating point value. This, along with the type are put into a list of objects, which is then used to calculate the final grade alongside 
the list of weights..
