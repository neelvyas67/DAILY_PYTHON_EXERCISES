{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "36054bec-3a6a-4f5d-b74d-636997a30fd3",
   "metadata": {},
   "outputs": [],
   "source": [
    "1. \n",
    "```python\n",
    "d = {\"hallo\": \"hello\", \"buch\": \"book\", \"haus\": \"house\", \"katze\": \"cat\", \"hund\": \"dog\"}\n",
    "\n",
    "word = input(\"Enter a German word: \").lower()\n",
    "\n",
    "if word in d:\n",
    "    print(d[word])\n",
    "else:\n",
    "    print(\"Word not found\")\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b6cc385c-4957-4504-aff3-5218a5003767",
   "metadata": {},
   "outputs": [],
   "source": [
    "2.\n",
    "```python\n",
    "numbers = []\n",
    "\n",
    "for i in range(8):\n",
    "    numbers.append(int(input(\"Enter a number: \")))\n",
    "\n",
    "print(set(numbers))\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5a7b4c80-e598-4614-9059-1d8df329f9a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 3. Can a set contain 18 (int) and '18' (str)?\n",
    "\n",
    "s = {18, '18'}\n",
    "\n",
    "print(s)\n",
    "\n",
    "# Output: {18, '18'}\n",
    "# Explanation: An integer and a string are different values."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2e48f435-f76a-4942-89ee-f4b4d50c824d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 4. What will be the length of set s?\n",
    "\n",
    "s = set()\n",
    "s.add(20)\n",
    "s.add(20.0)\n",
    "s.add('20')\n",
    "\n",
    "print(len(s))\n",
    "\n",
    "# Output: 2\n",
    "# Explanation: 20 and 20.0 are equal, so only one is stored.\n",
    "# The string '20' is a different value."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "19e6615e-057c-4241-87b6-efc750fb25df",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 5. What is the type of s?\n",
    "\n",
    "s = {}\n",
    "\n",
    "print(type(s))\n",
    "\n",
    "# Output: <class 'dict'>\n",
    "# Explanation: Empty curly braces create a dictionary.\n",
    "# To create an empty set, use s = set()."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "031f9801-c4e8-40d9-b8e7-be7dd3c43887",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "6.\n",
    "```python\n",
    "friends = {}\n",
    "\n",
    "for i in range(4):\n",
    "    name = input(\"Enter name: \")\n",
    "    language = input(\"Enter favorite language: \")\n",
    "    friends[name] = language\n",
    "\n",
    "print(friends)\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "63456081-5b5a-4912-8a45-ffd03e0a79d6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 7. What happens if two friends have the same name?\n",
    "\n",
    "friends = {}\n",
    "\n",
    "friends[\"Ali\"] = \"Python\"\n",
    "friends[\"Ali\"] = \"Java\"\n",
    "\n",
    "print(friends)\n",
    "\n",
    "# Output: {'Ali': 'Java'}\n",
    "# Explanation: The second value replaces the first value\n",
    "# because dictionary keys must be unique."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cdc6d556-90c1-4ac6-bdfa-3be97f1c862c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 8. What happens if two friends have the same favorite language?\n",
    "\n",
    "friends = {\n",
    "    \"Ali\": \"Python\",\n",
    "    \"Sara\": \"Python\"\n",
    "}\n",
    "\n",
    "print(friends)\n",
    "\n",
    "# Output: {'Ali': 'Python', 'Sara': 'Python'}\n",
    "# Explanation: Both friends remain in the dictionary\n",
    "# because dictionary values can be duplicated."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6af77848-701e-4778-9abd-518beddc0ceb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 9. Can you change the values inside a list contained in set s?\n",
    "\n",
    "s = {8, 7, 12, \"Riya\", [1, 2]}\n",
    "\n",
    "# Output:\n",
    "# TypeError: unhashable type: 'list'\n",
    "\n",
    "# Explanation: Lists cannot be stored in sets because\n",
    "# lists are mutable and unhashable.\n",
    "\n",
    "# Correct example using a tuple:\n",
    "s = {8, 7, 12, \"Riya\", (1, 2)}\n",
    "\n",
    "print(s)\n",
    "\n",
    "# Output: A set containing 8, 7, 12, 'Riya', and (1, 2)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cb938b3d-b8f7-46e5-9d98-f341e2320d0e",
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
