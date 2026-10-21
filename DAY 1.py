{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "271bf050-d749-4505-a0fc-7de24d9e13e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pyttsx3\n",
    "pyttsx3.speak(\"I will speak this text\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f81bdcc5-641c-4ae0-b530-4c2c7343b9a7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The sum of 3 and 6 is 9\n"
     ]
    }
   ],
   "source": [
    "#QUESTION 1\n",
    "# This program adds two numbers\n",
    "\n",
    "num1 = 3\n",
    "num2 = 6\n",
    "\n",
    "sum = num1 + num2\n",
    "\n",
    "\n",
    "print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "39af92e1-e070-45c0-a2e9-cd8197d52557",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the number (dividend):  2\n",
      "Enter the divisor (z):  8\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The remainder when 2.0 is divided by 8.0 is: 2.0\n"
     ]
    }
   ],
   "source": [
    "#QUESTION 2\n",
    "def find_remainder():\n",
    "    try:\n",
    "        \n",
    "        number = float(input(\"Enter the number (dividend): \"))\n",
    "        \n",
    "        \n",
    "        z = float(input(\"Enter the divisor (z): \"))\n",
    "        \n",
    "        \n",
    "        remainder = number % z\n",
    "        \n",
    "        print(f\"The remainder when {number} is divided by {z} is: {remainder}\")\n",
    "        \n",
    "    except ZeroDivisionError:\n",
    "        print(\"Error: Division by zero is not allowed. Please enter a value for 'z' other than 0.\")\n",
    "    except ValueError:\n",
    "        print(\"Error: Please enter valid numerical values.\")\n",
    "\n",
    "\n",
    "find_remainder()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "72b44cfd-1f02-430a-8327-c442d9b79bf6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'int'>\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "#QUESTION 3\n",
    "# Values given\n",
    "a = 34\n",
    "b = 80\n",
    "\n",
    "# Check the type of a variable\n",
    "print(type(a))  \n",
    "\n",
    "# Use the comparison operator to check if a > b\n",
    "result = a > b\n",
    "\n",
    "print(result)  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "60ec0087-8193-4277-908f-ac5fbdaedcef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the first number:  10\n",
      "Enter the second number:  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The average of 10.0 and 5.0 is: 7.5\n"
     ]
    }
   ],
   "source": [
    "#QUESTION 4\n",
    "num1 = float(input(\"Enter the first number: \"))\n",
    "\n",
    "\n",
    "num2 = float(input(\"Enter the second number: \"))\n",
    "\n",
    "\n",
    "average = (num1 + num2) / 2\n",
    "\n",
    "\n",
    "print(f\"The average of {num1} and {num2} is: {average}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "b77f3baf-2e07-4230-a756-582b65b0da0a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The square of 4.0 is 16.0\n"
     ]
    }
   ],
   "source": [
    "#QUESTION 5\n",
    "user_input = input(\"Enter a number: \")\n",
    "\n",
    "\n",
    "number = float(user_input)\n",
    "\n",
    "\n",
    "square = number ** 2\n",
    "\n",
    "\n",
    "print(f\"The square of {number} is {square}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "56639cb9-45c1-4441-adb9-97d80104e9d5",
   "metadata": {},
   "outputs": [],
   "source": [
    "#EXERCISE 2\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b0810c0b-3b71-4e0e-844b-47cfc787cc26",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your name:  Neel\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Good Morning Neel\n"
     ]
    }
   ],
   "source": [
    "#Question 1\n",
    "name = input(\"Enter your name: \")\n",
    "print(\"Good Morning\", name)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b2512bb0-5b82-43ee-8647-8423e071a2d3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your name:  Neel\n",
      "Enter the date:  06 Aug\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Dear Neel,\n",
      "You are selected!\n",
      "06 Aug\n",
      "\n"
     ]
    }
   ],
   "source": [
    "#Question 2\n",
    "name = input(\"Enter your name: \")\n",
    "date = input(\"Enter the date: \")\n",
    "\n",
    "letter = '''\n",
    "Dear <|Name|>,\n",
    "You are selected!\n",
    "<|Date|>\n",
    "'''\n",
    "\n",
    "letter = letter.replace(\"<|Name|>\", name)\n",
    "letter = letter.replace(\"<|Date|>\", date)\n",
    "\n",
    "print(letter)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "397f0259-98fd-477b-a29a-7184b6e02067",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "14\n"
     ]
    }
   ],
   "source": [
    "#Question 3\n",
    "name = \"Alex is a good  student\"\n",
    "\n",
    "print(name.find(\"  \"))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "644d4a69-d719-4bd4-8aed-06bbb8d1eb02",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Alex is a good student\n"
     ]
    }
   ],
   "source": [
    "#Question 4\n",
    "name = \"Alex is a good  student\"\n",
    "\n",
    "print(name.replace(\"  \", \" \"))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a2b1fcd2-1a67-40bc-9b8a-f40f1a0a302d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dear Class,\n",
      "\tlets learn python with me.\n",
      "Thanks!\n"
     ]
    }
   ],
   "source": [
    "#Question 5\n",
    "letter = \"Dear Class,\\n\\tlets learn python with me.\\nThanks!\"\n",
    "\n",
    "print(letter)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "503f96fb-5d64-4047-a557-bd146d5afb9e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
