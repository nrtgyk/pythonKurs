{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Introduction to Python (1/3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Outline\n",
    "\n",
    "* Python Language\n",
    "* Anaconda\n",
    "* Jupyter\n",
    "* PyCharm\n",
    "* First steps\n",
    "* Comments\n",
    "* Basic Types\n",
    "* Operators\n",
    "* Operator Presedence\n",
    "* Reserved Words\n",
    "* String\n",
    "* Type conversion (casting)\n",
    "* Getting User Input \n",
    "* Control Flow\n",
    "* Comparison operators\n",
    "* What Is True?\n",
    "* if/elif/else\n",
    "* for/range\n",
    "* while/break/continue\n",
    "* Conditional Expressions"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Python Language\n",
    "\n",
    "Python is a programming language, as are C, Fortran, BASIC, PHP, etc. Some specific features of Python are as follows:\n",
    "\n",
    "* an interpreted (as opposed to compiled) language. Contrary to e.g. C or Fortran, one does not compile Python code before executing it. In addition, Python can be used **interactively**: many Python interpreters are available, from which commands and scripts can be executed.\n",
    "* a free software released under an **open-source** license: Python can be used and distributed free of charge, even for building commercial software.\n",
    "* **multi-platform:** Python is available for all major operating systems, Windows, Linux/Unix, MacOS X, etc.\n",
    "* a very **readable** language with clear non-verbose syntax\n",
    "* a language for which a large variety of high-quality packages are available for various applications, from web frameworks to scientific computing.\n",
    "* a language very **easy to interface with other languages**, in particular C and C++.\n",
    "* Some other features of the language are illustrated just below. For example, Python is an **object-oriented** language, with **dynamic typing** (the same variable can contain objects of different types during the course of a program).\n",
    "\n",
    "See https://www.python.org/about/ for more information about distinguishing features of Python."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Anaconda\n",
    "\n",
    "Anaconda is a completely free Python distribution (including for commercial use and redistribution). It includes more than 400 of the most popular Python packages for science, math, engineering, and data analysis. \n",
    "\n",
    "Download and install Anaconda for Windows (Python 3.x):\n",
    "\n",
    "https://www.anaconda.com/distribution/"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Jupyter\n",
    "\n",
    "The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and explanatory text. \n",
    "\n",
    "The Jupyter Notebook: http://jupyter-notebook.readthedocs.io/en/latest/notebook.html\n",
    "\n",
    "Command line interaction:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": "0",
   "metadata": {
    "scrolled": "1",
   },
   "outputs": [],
   "source": [
    "print('Hello world')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## PyCharm\n",
    "\n",
    "PyCharm is an Integrated Development Environment (IDE) used for programming in Python. It provides code analysis, a graphical debugger, an integrated unit tester, integration with version control systems (VCSes), and supports web development with Django. PyCharm is developed by the Czech company JetBrains.\n",
    "\n",
    "It is cross-platform working on Windows, Mac OS X and Linux. PyCharm has a Professional Edition, released under a proprietary license and a Community Edition released under the Apache License. **PyCharm Community Edition** is less extensive than the Professional Edition.\n",
    "\n",
    "https://www.jetbrains.com/pycharm/download/#section=windows (Community Edition)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## First steps"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": "0",
   "metadata": {
    "scrolled": 0
   },
   "outputs": [],
   "source": [
    "print(\"Hello, world!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The message “Hello, world!” is then displayed. You just executed your first Python instruction, congratulations!\n",
    "To get yourself started, type the following stack of instructions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "scrolled": True
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "a = 3\n",
    "b = 2*a\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "int"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b = 'hello'\n",
    "type(b)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Two variables a and b have been defined above. Note that one does not declare the type of an variable before assigning its value. In C, conversely, one should write:\n",
    "\n",
    "```c\n",
    "int a = 3;\n",
    "```\n",
    "In addition, the type of a variable may change, in the sense that at one point in time it can be equal to a value of a certain type, and a second point in time, it can be equal to a value of a different type. \n",
    "\n",
    "_b_ was first equal to an integer, but it became equal to a string when it was assigned the value 'hello'. \n",
    "\n",
    "## Comments\n",
    "\n",
    "A comment is a piece of text in your program that is ignored by the Python interpreter. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# This is a comment"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Basic types\n",
    "\n",
    "**Numerical Types:**\n",
    "\n",
    "* Integer\n",
    "* Float\n",
    "* Complex\n",
    "* Boolean\n",
    "\n",
    "**Containers:**\n",
    "\n",
    "* String\n",
    "* List\n",
    "* Dictionary\n",
    "* Tuple\n",
    "* Set\n",
    "\n",
    "## Numerical Types\n",
    "\n",
    "Python supports the following numerical, scalar types: Integer, Floats, Complex, Booleans.\n",
    "\n",
    "### Integer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "1 + 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "int"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = 4\n",
    "type(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid token (<ipython-input-7-8922c565fd6b>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-7-8922c565fd6b>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    05 % Syntax Error\u001b[0m\n\u001b[0m     ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid token\n"
     ]
    }
   ],
   "source": [
    "05 % Syntax Error"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### How Big Is an int?\n",
    "\n",
    "In Python 2, the size of an int was limited to 32 bits. This was enough room to store any integer from –2,147,483,648 to 2,147,483,647.\n",
    "\n",
    "A **long** had even more room: 64 bits, allowing values from –9,223,372,036,854,775,808 to 9,223,372,036,854,775,807.\n",
    "\n",
    "In Python 3, long is long gone, and an int can be any size — even greater than 64 bits. \n",
    "\n",
    "Thus, you can say things like the following (10\\**100 is called a googol, and was the original name of Google before they decided on the easier spelling):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "googol = 10**100\n",
    "googol"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "googol * googol"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "int"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(googol)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Float"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "c = 2.1\n",
    "type(c) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Complex"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = 1.5 + 0.5j\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "type(1. + 0j) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a.real"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a.imag"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can also define complex numbers using the complex() function:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = complex(2, 3)\n",
    "a"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can add and subtract complex numbers in the same way as real numbers:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "b = 3 + 3j\n",
    "b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a + b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a * b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a / b"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The modulus (%) and the floor division (//) operations are not valid for complex numbers."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Boolean"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "3 > 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test = (3 > 4)\n",
    "test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "bool"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(test) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Operators \n",
    "\n",
    "\n",
    "![Operators](images/01/operators.png)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "7 * 3."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "2**10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "8 % 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "4 + 3 - 2 - 1 + 6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "ename": "ZeroDivisionError",
     "evalue": "division by zero",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mZeroDivisionError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-14-9e1622b385b6>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;36m1\u001b[0m\u001b[0;34m/\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mZeroDivisionError\u001b[0m: division by zero"
     ]
    }
   ],
   "source": [
    "1/0"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Operator Presedence\n",
    "\n",
    "![Operator Presedence](images/01/operator-presedence.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Reserved Words\n",
    "\n",
    "![Reserved Words](images/01/reserved-words.png)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "can't assign to keyword (<ipython-input-15-a3ee883b1482>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-15-a3ee883b1482>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    False = 3\u001b[0m\n\u001b[0m             ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m can't assign to keyword\n"
     ]
    }
   ],
   "source": [
    "False = 3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## String\n",
    "\n",
    "Different string syntaxes (simple, double or triple quotes):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Hello, how are you?'"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s = 'Hello, how are you?'\n",
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "s = \"Hi, what's up\"\n",
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "s = '''Hello,                 # tripling the quotes allows the\n",
    "       how are you'''         # the string to span more than one line\n",
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "s = \"\"\"Hi,\n",
    "what's up?\"\"\"\n",
    "s"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "```python\n",
    "In [1]: 'Hi, what's up?'\n",
    "------------------------------------------------------------\n",
    "   File \"<ipython console>\", line 1\n",
    "    'Hi, what's up?'\n",
    "           ^\n",
    "SyntaxError: invalid syntax\n",
    "```\n",
    "\n",
    "The newline character is **\\n**, and the tab character is **\\t**.\n",
    "\n",
    "Strings are collections like lists. Hence they can be _indexed_ and _sliced_, using the same syntax and rules.\n",
    "\n",
    "### Indexing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello'"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = \"hello\"\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'h'"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(a[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'e'"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a[-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a[-2]\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "(Remember that negative indices correspond to counting from the right end.)\n",
    "\n",
    "### Slicing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'lo,'"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = \"hello, world!\"\n",
    "a[3:6] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'lo o'"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a[2:10:2] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a[::3]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Accents and special characters can also be handled in Unicode strings (see https://docs.python.org/tutorial/introduction.html#unicode-strings).\n",
    "\n",
    "A string is an **immutable object** and it is not possible to modify its contents. One may however create new strings from the original one.\n",
    "\n",
    "```python\n",
    "In [53]: a = \"hello, world!\"\n",
    "In [54]: a[2] = 'z'\n",
    "---------------------------------------------------------------------------\n",
    "Traceback (most recent call last):\n",
    "   File \"<stdin>\", line 1, in <module>\n",
    "TypeError: 'str' object does not support item assignment\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Hello Levent'"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = \"Hello\"\n",
    "a = a + \" Levent\"\n",
    "a"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### String formatting"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'An integer: 1; a float: 0.1; another string: string'"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'An integer: {}; a float: {}; another string: {}'.format(1, 0.1, 'string')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "i = 102\n",
    "filename = '{}.txt'.format(i)\n",
    "filename"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Escape with \\"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "palindrome = 'A man,\\nA plan,\\nA canal:\\nPanama.'\n",
    "palindrome"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(palindrome)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print('a\\tbc')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "testimony = \"\\\"I did nothing!\\\" he said. \\\"Not that either! Or the other thing.\\\"\"\n",
    "print(testimony)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Combine with +"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "'Release the kraken! ' + 'At once!'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = \"My word! \" \"A gentleman caller!\"\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = 'Duck.'\n",
    "b = a\n",
    "c = 'Grey Duck!'\n",
    "a + b + c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(a, b, c)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Duplicate with *"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Na Na Na Na \\n'"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "start = 'Na ' * 4 + '\\n'\n",
    "start"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Get Length with len()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "letters = 'abcdefghijklmnopqrstuvwxyz'\n",
    "len(letters)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "empty = \"\"\n",
    "len(empty)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Split with split()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['get gloves', 'get mask', 'give cat vitamins', 'call ambulance']"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "todos = 'get gloves,get mask,give cat vitamins,call ambulance'\n",
    "a = todos.split(',')\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'get gloves'"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If you don’t specify a separator, split() uses any sequence of white space characters—newlines, spaces, and tabs."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "todos.split()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What if you have more than one separator string in a row in your original string? Well, you get an empty string as a list item:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "splitme = 'a/b//c/d///e'\n",
    "splitme.split('/')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Combine with join()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Yeti, Bigfoot, Loch Ness Monster\n"
     ]
    }
   ],
   "source": [
    "a = ['Yeti', 'Bigfoot', 'Loch Ness Monster']\n",
    "a_str = ', '.join(a)\n",
    "print(a_str)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "b_str = ''.join(a)\n",
    "b_str"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### startswith(), endswith(), find(), rfind() and count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "poem = '''All that doth flow we cannot liquid name\n",
    "Or else would fire and water be the same;\n",
    "But that is liquid which is moist and wet\n",
    "Fire that property can never get.\n",
    "Then 'tis not cold that doth the fire put out\n",
    "But 'tis the wet that makes it die, no doubt.'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "poem[:13]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "len(poem)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "poem.startswith('All')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "poem.endswith('That\\'s all, folks!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "word = 'the'\n",
    "poem.find(word)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "poem.rfind(word)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "poem.count(word)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### isalnum()\n",
    "\n",
    "Are all of the characters in the poem either letters or numbers (alphanumeric characters)?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "poem.isalnum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Nope, there were some punctuation characters."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "test = \"Deneme234\"\n",
    "test.isalnum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test = \"Deneme 234\"\n",
    "test.isalnum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test = \"Atatürk\"\n",
    "test.isalnum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Case and Alignment - strip(), capitalize(), title(), upper(), lower(), swapcase(), center(), ljust() and rjust()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "s = \"  aaa \"\n",
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "s.strip()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "setup = 'a duck goes into a bar...'\n",
    "setup.strip('.')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Capitalize the first word:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "setup.capitalize()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Capitalize all the words:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "setup.title()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "setup.upper()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "temp = \"Merhaba Dunya!\"\n",
    "temp.lower()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Swap upper- and lowercase:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "temp.swapcase()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "setup"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Center the string within 30 spaces:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "setup.center(30)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "setup.ljust(30)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "setup.rjust(30)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Substitute with replace()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "setup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "setup.replace('duck', 'marmoset')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Change up to 1 of them:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "setup.replace('a ', 'a famous ', 1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Type conversion (casting)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### int()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "int(1.2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "int(1.6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "int(True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "int(False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "int('99')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "int('-23')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "int('99 bottles of milk on the wall')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "int() will make integers from floats or strings of digits, but won’t handle strings con‐\n",
    "taining decimal points or exponents:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "int('98.6')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "True + 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### float()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "float(True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "float(False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "float(98)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "float('98.6')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "float('1.0e4')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "False + 5.0"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### str()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "str(98.6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "str(1.0e4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "str(True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The boolean value False is treated as 0 or 0.0 when mixed with integers or floats, and True is treated as 1 or 1.0:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Getting User Input\n",
    "\n",
    "As we start to write programs, it will help to have a nice, simple way to accept user input via the **input()** function. That way, we can write programs that ask a user to input a number, perform specific operations on that number, and then display the results of the operations. Let’s see it in action:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = input()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Notice the single quotes around 1. The input() function returns the input as a string.\n",
    "\n",
    "Even if the only characters in a string are numbers, Python won’t treat that string as a number unless we get rid of those quotation marks. So before we can perform any mathematical operations with the input, we’ll have to convert it into the correct number type. A string can be converted to an integer or floating point number using the **int()** or **float()** function, respectively:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = '1'\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "a + 2 # Error!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "int(a) + 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "float(a) + 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If you take a string that has a floating point number (like '2.5' or even '2.0') and input that string into the int() function, you’ll get an error message:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "int('2.0')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Similarly, when you supply a fractional number such as **3/4** as an input, Python cannot convert it into an equivalent floating point number or integer. Once again, a **ValueError** exception is raised:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = float(input())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Handling Exceptions and Invalid Input**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "try:\n",
    "    a = float(input('Enter a number: ')) # 3/4\n",
    "except ValueError:\n",
    "    print('You entered an invalid number')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can combine the input and conversion in a single statement, as follows:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = int(input())\n",
    "x = a + 1\n",
    "x"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This works great if the user inputs an integer. But as we saw earlier, if the input is a floating point number (even one that’s equivalent to an integer, like 1.0), this will produce an error:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = int(input()) # Enter 1.0"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Complex Numbers as Input**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**complex()** function can convert a string such as '2+3j' into a complex number:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "z = complex(input('Enter a complex number: ')) # Enter 2+3j\n",
    "z"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If you enter the string as '2 + 3j' (with spaces), it will result in a ValueError error message:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "z = complex(input('Enter a complex number: ')) # Enter 2 + 3j"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Control Flow\n",
    "\n",
    "Controls the order in which the code is executed.\n",
    "\n",
    "* Comparison operators\n",
    "* What Is True?\n",
    "* if/elif/else\n",
    "* for/range\n",
    "* while/break/continue\n",
    "* Conditional Expressions"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Comparison operators\n",
    "\n",
    "Comparison operators are:\n",
    "\n",
    "* equality ==\n",
    "* inequality !=\n",
    "* less than <\n",
    "* less than or equal <=\n",
    "* greater than >\n",
    "* greater than or equal >=\n",
    "* membership in …"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "x = 7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "x == 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "x == 7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "5 < x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "x < 10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "(5 < x) and (x < 10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "5 < x and x < 10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "5 < x or x < 10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "5 < x and not x > 10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "(5 < x) and (x < 10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "5 < x < 10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "5 < x < 10 < 999"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What Is True?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What if the element we’re checking isn’t a boolean? What does Python consider True and False?\n",
    "\n",
    "A false value doesn’t necessarily need to explicitly be False. For example, these are all considered False:\n",
    "\n",
    "* boolean: False\n",
    "* null: None\n",
    "* zero integer: 0\n",
    "* zero float: 0.0\n",
    "* empty string: ''\n",
    "* empty list: []\n",
    "* empty tuple: ()\n",
    "* empty dict: {}\n",
    "* empty set: ()\n",
    "\n",
    "Anything else is considered True. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## if/elif/else"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Obvious!\n"
     ]
    }
   ],
   "source": [
    "if 2**2 == 4:\n",
    "    print('Obvious!')\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hey, it's empty!\n"
     ]
    }
   ],
   "source": [
    "some_list = []\n",
    "if some_list:\n",
    "    print(\"There's something in here\")\n",
    "else:\n",
    "    print(\"Hey, it's empty!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Blocks are delimited by indentation\n",
    "\n",
    "Type the following lines in your Python interpreter, and be careful to respect the indentation depth. The Ipython shell automatically increases the indentation depth after a column : sign; to decrease the indentation depth, go **four spaces** to the left with the Backspace key. Press the Enter key twice to leave the logical block."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a=10\n",
    "\n",
    "if a == 1:\n",
    "    print(1)\n",
    "elif a == 2:\n",
    "    print(2)\n",
    "else:\n",
    "    print('A lot')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## for/range\n",
    "\n",
    "Iterating with an index:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "for i in [0, 1, 2, 3]:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "range(0, 4)"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "range(4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "for i in range(4):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in range(1,4):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "But most often, it is more readable to iterate over values:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "for word in ['cool', 'powerful', 'readable']:\n",
    "    print('Python is %s' % word)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## while/break/continue\n",
    "\n",
    "Typical C-style while loop (Mandelbrot problem):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "z = 5\n",
    "\n",
    "while z > 2:    \n",
    "    print(z)\n",
    "    z = z - 1\n",
    "\n",
    "z"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**break** out of enclosing for/while loop:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "z = 5\n",
    "\n",
    "while z > 2: \n",
    "    if z == 3:\n",
    "        break\n",
    "    z = z - 1\n",
    "    print(z)\n",
    "z"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**continue** the next iteration of a loop:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = [1, 0, 2, 4]\n",
    "\n",
    "for element in a:\n",
    "    if element == 0:\n",
    "        continue\n",
    "    print(1. / element)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Conditional Expressions\n",
    "\n",
    "![Conditional Expressions](images/01/cond_expr.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Example:** Find the sum of integers between 0 and a number given by the user."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Maksimum sayıyı girin: 2.3\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: '2.3'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-41-43a9dff0baf9>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0ms\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'Maksimum sayıyı girin: '\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0msayi\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ms\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m \u001b[0msum\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0ma\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0msayi\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m     \u001b[0msum\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0msum\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0ma\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mValueError\u001b[0m: invalid literal for int() with base 10: '2.3'"
     ]
    }
   ],
   "source": [
    "s = input('Maksimum sayıyı girin: ')\n",
    "sayi = int(s)\n",
    "sum = 0\n",
    "for a in range(0, sayi+1):\n",
    "    sum = sum + a\n",
    "\n",
    "print(sum)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
