{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a64dacd5-9876-4adb-88b6-caf89de54f94",
   "metadata": {},
   "outputs": [],
   "source": [
    "def validate_input(data):\n",
    "    errors = []\n",
    "\n",
    "    if not (0 < data[\"age\"] < 120):\n",
    "        errors.append(\"العمر غير صحيح\")\n",
    "\n",
    "    if not (50 < data[\"trestbps\"] < 250):\n",
    "        errors.append(\"ضغط الدم غير صحيح\")\n",
    "\n",
    "    if not (100 < data[\"chol\"] < 600):\n",
    "        errors.append(\"الكوليسترول غير صحيح\")\n",
    "\n",
    "    if not (0 <= data[\"oldpeak\"] <= 10):\n",
    "        errors.append(\"oldpeak غير صحيح\")\n",
    "\n",
    "    return errors"
   ]
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
