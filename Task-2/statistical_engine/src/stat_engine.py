import math

class StatEngine:
    def __init__(self, data):
        if len(data) == 0:
            raise ValueError("Data cannot be empty")

        self.data = []
        for item in data:
            if isinstance(item, (int, float)):
                self.data.append(item)
            else:
                try:
                    self.data.append(float(item))
                except:
                    continue

        if len(self.data) == 0:
            raise TypeError("No valid numeric data")

    # -------- Mean --------
    def get_mean(self):
        total = 0
        count = 0

        for num in self.data:
            total = total + num
            count = count + 1

        return total / count

    # -------- Median --------
    def get_median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)

        if n % 2 == 1:
            middle_index = n // 2
            return sorted_data[middle_index]
        else:
            middle1 = sorted_data[n // 2 - 1]
            middle2 = sorted_data[n // 2]
            return (middle1 + middle2) / 2

    # -------- Mode --------
    def get_mode(self):
        frequency = {}

        for num in self.data:
            if num in frequency:
                frequency[num] = frequency[num] + 1
            else:
                frequency[num] = 1

        max_count = 0
        for value in frequency.values():
            if value > max_count:
                max_count = value

        if max_count == 1:
            return "No mode (all values unique)"

        modes = []
        for key in frequency:
            if frequency[key] == max_count:
                modes.append(key)

        return modes

    # -------- Variance --------
    def get_variance(self, is_sample=True):
        mean = self.get_mean()
        total = 0

        for num in self.data:
            diff = num - mean
            total = total + (diff * diff)

        n = len(self.data)

        if is_sample:
            if n < 2:
                raise ValueError("Need at least 2 values for sample variance")
            return total / (n - 1)
        else:
            return total / n

    # -------- Standard Deviation --------
    def get_standard_deviation(self, is_sample=True):
        variance = self.get_variance(is_sample)
        return math.sqrt(variance)

    # -------- Outliers --------
    def get_outliers(self, threshold=2):
        mean = self.get_mean()
        std = self.get_standard_deviation()

        outliers = []

        for num in self.data:
            z = abs(num - mean) / std
            if z > threshold:
                outliers.append(num)

        return outliers