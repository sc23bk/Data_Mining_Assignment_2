# Answer found in Q5 in Question Bank 1 (Tan et al, 2nd ed)

# import student_code_with_answers.utils as u
import utils as u


# Example of how to specify a binary with the structure:
# See the file INSTRUCTIONS.md
# ----------------------------------------------------------------------


def question1():
    """
    Note 1: Each attribute can appear as a node in the tree AT MOST once.
    Note 2: For level two, fill the keys for all cases left and right. If and attribute
    is not considered for level 2, set the values to -1. For example, if "flu" were the
    choice for level 1 (it is not), then set level2_left['flu'] = level2_right['flu'] = -1.,
    and the same for keys 'flu_info_gain'.
    """
    answer = False
    answer = {}
    level1 = {}
    level2_left = {}
    level2_right = {}

    level1["smoking"] = 1.0
    level1["smoking_info_gain"] = 0.2780719051126377

    level1["cough"] = -1.0
    level1["cough_info_gain"] = -1.0

    level1["radon"] = -1.0
    level1["radon_info_gain"] = -1.0

    level1["weight_loss"] = -1.0
    level1["weight_loss_info_gain"] = -1.0

    level2_left["smoking"] = -1.0
    level2_left["smoking_info_gain"] = -1.0
    level2_right["smoking"] = -1.0
    level2_right["smoking_info_gain"] = -1.0

    level2_left["radon"] = 1.0
    level2_left["radon_info_gain"] = 0.0

    level2_left["cough"] = 0.8812908992306927
    level2_left["cough_info_gain"] = 0.7219280948873623

    level2_left["weight_loss"] = -1.0
    level2_left["weight_loss_info_gain"] = -1.0

    level2_right["radon"] = 0.7219280948873623
    level2_right["radon_info_gain"] = 0.7219280948873623

    level2_right["cough"] = -1.0
    level2_right["cough_info_gain"] = -1.0

    level2_right["weight_loss"] = -1.0
    level2_right["weight_loss_info_gain"] = -1.0

    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right

    # Fill up `construct_tree``
    # tree, training_error = construct_tree()
    tree = u.BinaryTree("smoking")  # MUST STILL CREATE THE TREE *****
    A = tree.insert_left("Chronic Cough")
    B = tree.insert_right("Radon")
    A.insert_left("Yes")
    A.insert_right("No")
    B.insert_left("Yes")
    B.insert_right("No")
    tree.print_tree()
    
    answer["tree"] = tree  # use the Tree structure
    # answer["training_error"] = training_error
    answer["training_error"] = 0.0  

    return answer
    

# ----------------------------------------------------------------------


def question2():
    answer = {}

    # Answers are floats
    answer["(a) entropy_entire_data"] = 1.0
    # Infogain
    answer["(b) x <= 0.2"] = 0.46438561897747244
    answer["(b) x <= 0.7"] = 0.3602012209808308
    answer["(b) y <= 0.6"] = 0.44217935649972373

    # choose one of 'x=0.2', 'x=0.7', or 'x=0.6'
    answer["(c) attribute"] = "x = 0.7"  

    # Use the Binary Tree structure to construct the tree
    # Answer is an instance of BinaryTree
    tree = u.BinaryTree("y = 0.7")
    tree.insert_left("x=0.7")
    tree.left.insert_left("B")
    tree.left.insert_right("y=0.3")
    tree.left.right.insert_left("A")
    tree.left.right.insert_right("C")

    tree.insert_right("x=0.2")
    tree.right.insert_left("y=0.8")
    tree.right.insert_right("A")
    tree.right.left.insert_left("C")
    tree.right.left.insert_right("B")
    tree.print_tree()
    answer["(d) full decision tree"] = tree

    return answer


# ----------------------------------------------------------------------


def question3():
    answer = {}

    # float
    answer["(a) Gini, overall"] = 0.5

    # float
    answer["(b) Gini, ID"] = 0.0
    answer["(c) Gini, Gender"] = 0.48
    answer["(d) Gini, Car type"] = 0.1625
    answer["(e) Gini, Shirt type"] = 0.4914

    answer["(f) attr for splitting"] = "Car type"

    # Explanatory text string
    answer["(f) explain choice"] = "The attribute car type is used for splitting at the root node because it has the lowest Gini index"

    return answer


# ----------------------------------------------------------------------
# Answers in th form [str1, str2, str3]
# If both 'binary' and 'discrete' apply, choose 'binary'.
# str1 in ['binary', 'discrete', 'continuous']
# str2 in ['qualitative', 'quantitative']
# str3 in ['interval', 'nominal', 'ratio', 'ordinal']


def question4():
    answer = {}

    # [string, string, string]
    # Each string is one of ['binary', 'discrete', 'continuous', 'qualitative', 'nominal', 'ordinal',
    #  'quantitative', 'interval', 'ratio'
    # If you have a choice between 'binary' and 'discrete', choose 'binary'

    answer["a"] = [binary, qualitative, nominal]

    # Explain if there is more than one interpretation. Repeat for the other questions. At least five words that form a sentence.
    answer["a: explain"] = "Just two categories, AM or PM, with no order."

    answer["b"] = [continuous, quantitative, ratio]
    answer["b: explain"] = "Continuous, because brightness can vary over a continuous range."

    answer["c"] = [discrete, qualitative, ordinal]
    answer["c: explain"] = " People's judgments of brightness are categorized into discrete levels (e.g., very bright, bright, dim)"

    answer["d"] = [continuous, quantitative, interval]
    answer["d: explain"] = "Angle measurement is interval rather than ratio since it lacks a genuine zero, even if 0 and 360 degrees indicate the same place."

    answer["e"] = [discrete, qualitative, ordinal]
    answer["e: explain"] = "These awards don't measure the amount that separates the three main categories, which are naturally arranged according to achievement level."

    answer["f"] = [continuous, quantitative, ratio]
    answer["f: explain"] = "Height can vary over a continuous range"

    answer["g"] = [discrete, quantitative, ratio)]
    answer["g: explain"] = "The number of patients is countable"

    answer["h"] = [discrete, qualitative, nominal]
    answer["h: explain"] = "ISBN numbers are unique identifiers for books and do not have a quantitative value or order."

    answer["i"] = [discrete, qualitative, ordinal]
    answer["i: explain"] = "These categories are not strictly numerically measurable, but they have a natural order based on the quantity of light that may travel through."

    answer["j"] = [discrete, qualitative, ordinal]
    answer["j: explain"] = "Military ranks have a clear hierarchical order but do not represent a quantitative measurement."

    answer["k"] = [continuous, quantitative, ratio]
    answer["k: explain"] = "Distance has a real zero point at its center and can be measured on a continuous scale, ratio calculations may be made using it."

    answer["l"] = [continuous, quantitative, ratio]
    answer["l: explain"] = "Density can vary over a continuous range, and allows for the comparison of ratios."

    answer["m"] = [discrete, qualitative, nominal]
    answer["m: explain"] = "Coat check numbers are used for identification and do not have a quantitative value or order."

    return answer


# ----------------------------------------------------------------------


def question5():
    explain = {}

    # Read appropriate section of book chapter 3

    # string: one of 'Model 1' or 'Model 2'
    explain["a"] = "Model 2"
    explain["a explain"] = "Model 2 better handles unknown data due to its increased testing accuracy. Model 1 looks overfitted given how much higher the training accuracy is than the testing accuracy."

    # string: one of 'Model 1' or 'Model 2'
    explain["b"] = "Model 2"
    explain["b explain"] = "The measurements shown are only the means of the accuracy values from the two datasets. Model 2 is still more accurate when it comes to Dataset B, or the actual unseen data, even if both models were trained on Dataset A, so they will always get them correct."

    explain["c similarity"] = "Incorporation of Model Complexity"
    explain["c similarity explain"] = "Penalizing decision tree complexity is the aim of both MDL and pessimistic error estimation strategies. They aim to find a middle ground between the size or complexity of the tree and its capacity to match the training data, assuming that simpler models generalize better to unknown data."

    explain["c difference"] = "Approach to Model Complexity"
    explain["c difference explain"] = "The MDL Principle requires a trade-off between the model's fit to the data and its complexity, which is dictated by how long the description has to be in order to encapsulate the model. However, by adding a penalty factor that increases in complexity along with the decision tree (such as the number of leaf nodes), the Pessimistic Error Estimate directly modifies the error estimate of the tree."

    return explain


# ----------------------------------------------------------------------
def question6():
    answer = {}
    # x <= ? is the left branch
    # y <= ? is the left branch

    # value of the form "z <= float" where "z" is "x" or "y"
    #  and "float" is a floating point number (notice: <=)
    # The value could also be "A" or "B" if it is a leaf
    answer["a, level 1"] = ""
    answer["a, level 2, right"] =""
    answer["a, level 2, left"] = ""
    answer["a, level 3, left"] = ""
    answer["a, level 3, right"] = ""

    # run each datum through the tree. Count the number of errors and divide by number of samples. .
    # Since we have areas: calculate the area that is misclassified (total area is unity)
    # float between 0 and 1
    answer["b, expected error"] = 0.

    # Use u.BinaryTree to define the tree. Create your tree.
    # Replace "root node" by the proper node of the form "z <= float"
    tree = u.BinaryTree("root note")

    answer["c, tree"] = tree

    return answer


# ----------------------------------------------------------------------
def question7():
    answer = {}

    # float
    answer["a, info gain, ID"] = 1.0 
    answer["b, info gain, Handedness"] = 0.531 #Information Gain=Entropy(S)−( 10/20 Entropy(Left)+ 10/20 Entropy(Right))

    # string: "ID" or "Handedness"
    answer["c, which attrib"] = "ID" #According to the principle of information gain in decision tree algorithms, the attribute that results in the highest information gain is chosen for the split. Therefore, ID would be chosen as the splitting attribute.

    # answer is a float
    answer["d, gain ratio, ID"] = 0.2314 # gain ratio = info gain/ split info
    answer["e, gain ratio, Handedness"] = 0.53100 

    # string: one of 'ID' or 'Handedness' based on gain ratio
    # choose the attribute with the largest gain ratio
    answer["f, which attrib"] = "Handedness"

    return answer


# ----------------------------------------------------------------------

if __name__ == "__main__":
    answers = {}
    answers["q1"] = question1()
    answers["q2"] = question2()
    answers["q3"] = question3()
    answers["q4"] = question4()
    answers["q5"] = question5()
    answers["q6"] = question6()
    answers["q7"] = question7()

    u.save_dict("answers.pkl", answers)

