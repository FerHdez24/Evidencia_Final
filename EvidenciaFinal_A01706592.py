{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPn+e8OYkWYE3AM/J0A/Tqi",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/FerHdez24/Evidencia_Final/blob/main/EvidenciaFinal_A01706592.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kJ2F4iW0EvIZ",
        "outputId": "99a2dcd4-9113-4b89-993c-1533a0e7f486"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator()"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ],
      "source": [
        "import streamlit as st\n",
        "import pandas as pd\n",
        "\n",
        "\n",
        "st.title('Police Incident Reports from 2018 to 2020 in San Francisco')\n",
        "\n",
        "df = pd.read_csv(\"https://drive.google.com/file/d/1sUXMxryvguQp81yseLxYymTX5RxaH0e9/view?usp=drive_link/Police_Department_Incident_Reports__2018_to_Present.csv\")\n",
        "\n",
        "st.markdown('The data shown below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution.')\n",
        "\n",
        "mapa=pd.DataFrame()\n",
        "mapa=mapa.dropna()\n",
        "st.map(mapa.astype(int))"
      ]
    }
  ]
}