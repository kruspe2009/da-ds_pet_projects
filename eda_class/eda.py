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

    def values_ditribution(
        self, column, x_label="Распределение признака", title="Распределение", bins=20
    ):
        plt.figure(figsize=[16, 8])
        plt.hist(x=self[column], bins=bins, ec="black")
        plt.grid(axis="y", alpha=0.5)
        plt.xlabel(x_label, fontsize=12)
        plt.axvline(
            x=data[(~self[column].isna())][column].median(),
            color="r",
            label=f"Медиана: {round(data[(~self[column].isna())][column].median(), 2)}",
        )
        plt.axvline(
            x=np.percentile(self[column], 99),
            color="g",
            label=f"99й процентиль: {round(np.percentile(self[column], 99), 2)}",
        )
        plt.axvline(
            x=data[(~self[column].isna())][column].mean(),
            color="b",
            label=f"Среднее: {round(data[(~self[column].isna())][column].mean(), 2)}",
        )
        plt.legend()
        plt.title(title, fontsize=15)
        plt.show()
