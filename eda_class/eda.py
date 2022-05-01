class eda:
    def df_size(self):
        print(f"Количество строк в датафрейме: {self.shape[0]}")
        print(f"Количество столбцов в датафрейме: {self.shape[1]}")

    def full_duplicates(self, show_slice=False):
        if show_slice == False:
            print(f"Полных дубликатов в датафрейме: {self.duplicated().sum()}")
        else:
            print(f"Полных дубликатов в датафрейме: {self.duplicated().sum()}")
            print()
            if len(self[self.duplicated()]) != 0:
                return self[self.duplicated()]

    def gaps(self):
        gaps_pivot = self.isna().sum()
        dictionary = {}
        for index in gaps_pivot.index:
            if gaps_pivot[index] > 0:
                dictionary[index] = gaps_pivot[index]
        report = pd.DataFrame.from_dict(dictionary, orient="index").reset_index()
        report.columns = ["Столбец", "Количество пропусков"]
        report["% от датасета"] = report["Количество пропусков"] / len(self)
        return report
