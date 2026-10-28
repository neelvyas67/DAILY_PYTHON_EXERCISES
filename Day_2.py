{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "196b15d7-b404-49af-928c-b5989e7b41e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "DAY_2 Exercises"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8e6e6cd6-944c-4842-acd2-855261c311e7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter color 1:  Blue\n",
      "Enter color 2:  Green\n",
      "Enter color 3:  Red\n"
     ]
    }
   ],
   "source": [
    "#Question 1\n",
    "\n",
    "colors = [input(f\"Enter color {i+1}: \") for i in range(5)]\n",
    "print(\"The entered colors are:\", colors)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "411cfff4-48db-4ba9-8e8d-9dbb6d6511ea",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Question 2\n",
    "\n",
    "marks = []\n",
    "for i in range(7):\n",
    "    m = float(input(f\"Enter marks for student {i+1}: \"))\n",
    "    marks.append(m)\n",
    "\n",
    "marks.sort()\n",
    "print(\"Sorted marks:\", marks)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0f54ca36-d9cb-4bac-bbbd-3dd27c96e8a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Question 3\n",
    "\n",
    "my_tuple = (1, 2, 3)\n",
    "\n",
    "try:\n",
    "    my_tuple[0] = 10  # Tuples do not support item assignment\n",
    "except TypeError as e:\n",
    "    print(\"TypeError caught:\", e)\n",
    "    print(\"Conclusion: Tuple elements cannot be changed (tuples are immutable).\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "853b6b04-fb5a-44c8-a441-cdd5774ac60c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Question 4\n",
    "\n",
    "numbers = []\n",
    "for i in range(5):\n",
    "    n = float(input(f\"Enter number {i+1}: \"))\n",
    "    numbers.append(n)\n",
    "\n",
    "total_sum = sum(numbers)\n",
    "print(\"The sum of the 5 numbers is:\", total_sum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8c90e92e-7820-4c65-ae93-ee58159f9654",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Question 5\n",
    "\n",
    "a = (7, 0, 8, 0, 9, 0, 4, 5, 0, 0, 0)\n",
    "\n",
    "zero_count = a.count(0)\n",
    "print(\"Number of zeros in the tuple:\", zero_count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6999fedb-3a85-4485-b5d2-de68a1cb4e60",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c848d5f1-111e-4a3f-91d8-cb38065b351d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python (notebook-env)",
   "language": "python",
   "name": "notebook-env"
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
