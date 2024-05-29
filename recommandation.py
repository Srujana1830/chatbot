{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Recommendation_System.ipynb",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU",
    "widgets": {
      "application/vnd.jupyter.widget-state+json": {
        "3c1765cabeaf4d75a130311ddc4591a1": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "HBoxModel",
          "state": {
            "_view_name": "HBoxView",
            "_dom_classes": [],
            "_model_name": "HBoxModel",
            "_view_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_view_count": null,
            "_view_module_version": "1.5.0",
            "box_style": "",
            "layout": "IPY_MODEL_6db170b52f5a4f72afd083a3a9c157aa",
            "_model_module": "@jupyter-widgets/controls",
            "children": [
              "IPY_MODEL_69073fd458234bba829af9731b4fce1c",
              "IPY_MODEL_88151edb53134487b95f6bcbcd7fd2b4"
            ]
          }
        },
        "6db170b52f5a4f72afd083a3a9c157aa": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "state": {
            "_view_name": "LayoutView",
            "grid_template_rows": null,
            "right": null,
            "justify_content": null,
            "_view_module": "@jupyter-widgets/base",
            "overflow": null,
            "_model_module_version": "1.2.0",
            "_view_count": null,
            "flex_flow": null,
            "width": null,
            "min_width": null,
            "border": null,
            "align_items": null,
            "bottom": null,
            "_model_module": "@jupyter-widgets/base",
            "top": null,
            "grid_column": null,
            "overflow_y": null,
            "overflow_x": null,
            "grid_auto_flow": null,
            "grid_area": null,
            "grid_template_columns": null,
            "flex": null,
            "_model_name": "LayoutModel",
            "justify_items": null,
            "grid_row": null,
            "max_height": null,
            "align_content": null,
            "visibility": null,
            "align_self": null,
            "height": null,
            "min_height": null,
            "padding": null,
            "grid_auto_rows": null,
            "grid_gap": null,
            "max_width": null,
            "order": null,
            "_view_module_version": "1.2.0",
            "grid_template_areas": null,
            "object_position": null,
            "object_fit": null,
            "grid_auto_columns": null,
            "margin": null,
            "display": null,
            "left": null
          }
        },
        "69073fd458234bba829af9731b4fce1c": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "FloatProgressModel",
          "state": {
            "_view_name": "ProgressView",
            "style": "IPY_MODEL_9b185906b1dc465e93b9f058a1fec47a",
            "_dom_classes": [],
            "description": "100%",
            "_model_name": "FloatProgressModel",
            "bar_style": "success",
            "max": 128,
            "_view_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "value": 128,
            "_view_count": null,
            "_view_module_version": "1.5.0",
            "orientation": "horizontal",
            "min": 0,
            "description_tooltip": null,
            "_model_module": "@jupyter-widgets/controls",
            "layout": "IPY_MODEL_20b4738815cd467dba2946031d6d9027"
          }
        },
        "88151edb53134487b95f6bcbcd7fd2b4": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "HTMLModel",
          "state": {
            "_view_name": "HTMLView",
            "style": "IPY_MODEL_c279f9a0a0fe498b9db167a237517e6e",
            "_dom_classes": [],
            "description": "",
            "_model_name": "HTMLModel",
            "placeholder": "​",
            "_view_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "value": " 128/128 [03:03&lt;00:00,  1.44s/it]",
            "_view_count": null,
            "_view_module_version": "1.5.0",
            "description_tooltip": null,
            "_model_module": "@jupyter-widgets/controls",
            "layout": "IPY_MODEL_005a499c40bd407ca20c2492d9c4f170"
          }
        },
        "9b185906b1dc465e93b9f058a1fec47a": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ProgressStyleModel",
          "state": {
            "_view_name": "StyleView",
            "_model_name": "ProgressStyleModel",
            "description_width": "initial",
            "_view_module": "@jupyter-widgets/base",
            "_model_module_version": "1.5.0",
            "_view_count": null,
            "_view_module_version": "1.2.0",
            "bar_color": null,
            "_model_module": "@jupyter-widgets/controls"
          }
        },
        "20b4738815cd467dba2946031d6d9027": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "state": {
            "_view_name": "LayoutView",
            "grid_template_rows": null,
            "right": null,
            "justify_content": null,
            "_view_module": "@jupyter-widgets/base",
            "overflow": null,
            "_model_module_version": "1.2.0",
            "_view_count": null,
            "flex_flow": null,
            "width": null,
            "min_width": null,
            "border": null,
            "align_items": null,
            "bottom": null,
            "_model_module": "@jupyter-widgets/base",
            "top": null,
            "grid_column": null,
            "overflow_y": null,
            "overflow_x": null,
            "grid_auto_flow": null,
            "grid_area": null,
            "grid_template_columns": null,
            "flex": null,
            "_model_name": "LayoutModel",
            "justify_items": null,
            "grid_row": null,
            "max_height": null,
            "align_content": null,
            "visibility": null,
            "align_self": null,
            "height": null,
            "min_height": null,
            "padding": null,
            "grid_auto_rows": null,
            "grid_gap": null,
            "max_width": null,
            "order": null,
            "_view_module_version": "1.2.0",
            "grid_template_areas": null,
            "object_position": null,
            "object_fit": null,
            "grid_auto_columns": null,
            "margin": null,
            "display": null,
            "left": null
          }
        },
        "c279f9a0a0fe498b9db167a237517e6e": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "DescriptionStyleModel",
          "state": {
            "_view_name": "StyleView",
            "_model_name": "DescriptionStyleModel",
            "description_width": "",
            "_view_module": "@jupyter-widgets/base",
            "_model_module_version": "1.5.0",
            "_view_count": null,
            "_view_module_version": "1.2.0",
            "_model_module": "@jupyter-widgets/controls"
          }
        },
        "005a499c40bd407ca20c2492d9c4f170": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "state": {
            "_view_name": "LayoutView",
            "grid_template_rows": null,
            "right": null,
            "justify_content": null,
            "_view_module": "@jupyter-widgets/base",
            "overflow": null,
            "_model_module_version": "1.2.0",
            "_view_count": null,
            "flex_flow": null,
            "width": null,
            "min_width": null,
            "border": null,
            "align_items": null,
            "bottom": null,
            "_model_module": "@jupyter-widgets/base",
            "top": null,
            "grid_column": null,
            "overflow_y": null,
            "overflow_x": null,
            "grid_auto_flow": null,
            "grid_area": null,
            "grid_template_columns": null,
            "flex": null,
            "_model_name": "LayoutModel",
            "justify_items": null,
            "grid_row": null,
            "max_height": null,
            "align_content": null,
            "visibility": null,
            "align_self": null,
            "height": null,
            "min_height": null,
            "padding": null,
            "grid_auto_rows": null,
            "grid_gap": null,
            "max_width": null,
            "order": null,
            "_view_module_version": "1.2.0",
            "grid_template_areas": null,
            "object_position": null,
            "object_fit": null,
            "grid_auto_columns": null,
            "margin": null,
            "display": null,
            "left": null
          }
        }
      }
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NvcMQzFckjXd",
        "outputId": "b4424a9f-ffb3-4cfb-fd5b-9fbad8c29b4f"
      },
      "source": [
        "# Data Citation:\n",
        "# F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets: History and Context. ACM Transactions on \n",
        "# Interactive Intelligent Systems (TiiS) 5, 4: 19:1–19:19. <https://doi.org/10.1145/2827872>\n",
        "\n",
        "! curl http://files.grouplens.org/datasets/movielens/ml-latest-small.zip -o ml-latest-small.zip"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current\n",
            "                                 Dload  Upload   Total   Spent    Left  Speed\n",
            "100  955k  100  955k    0     0  3717k      0 --:--:-- --:--:-- --:--:-- 3731k\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "68BdqtQikvVE"
      },
      "source": [
        "import zipfile\n",
        "with zipfile.ZipFile('ml-latest-small.zip', 'r') as zip_ref:\n",
        "    zip_ref.extractall('data')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OmO7jmrpkvZf"
      },
      "source": [
        "# import the dataset\n",
        "import pandas as pd\n",
        "movies_df = pd.read_csv('data/ml-latest-small/movies.csv')\n",
        "ratings_df = pd.read_csv('data/ml-latest-small/ratings.csv')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Q-KRTGaskvdn",
        "outputId": "ec89b4c8-ee99-407c-ce07-8d9ddcf0f0b1"
      },
      "source": [
        "print('The dimensions of movies dataframe are:', movies_df.shape,'\\nThe dimensions of ratings dataframe are:', ratings_df.shape)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "The dimensions of movies dataframe are: (9742, 3) \n",
            "The dimensions of ratings dataframe are: (100836, 4)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 195
        },
        "id": "ALPeuAiBk0mM",
        "outputId": "8afc063a-7b73-4cdf-b624-cf36ecfa231a"
      },
      "source": [
        "# Take a look at movies_df\n",
        "movies_df.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>movieId</th>\n",
              "      <th>title</th>\n",
              "      <th>genres</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>Toy Story (1995)</td>\n",
              "      <td>Adventure|Animation|Children|Comedy|Fantasy</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>Jumanji (1995)</td>\n",
              "      <td>Adventure|Children|Fantasy</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>Grumpier Old Men (1995)</td>\n",
              "      <td>Comedy|Romance</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>Waiting to Exhale (1995)</td>\n",
              "      <td>Comedy|Drama|Romance</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>Father of the Bride Part II (1995)</td>\n",
              "      <td>Comedy</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   movieId  ...                                       genres\n",
              "0        1  ...  Adventure|Animation|Children|Comedy|Fantasy\n",
              "1        2  ...                   Adventure|Children|Fantasy\n",
              "2        3  ...                               Comedy|Romance\n",
              "3        4  ...                         Comedy|Drama|Romance\n",
              "4        5  ...                                       Comedy\n",
              "\n",
              "[5 rows x 3 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 195
        },
        "id": "KzPoqkWbk0oh",
        "outputId": "762a17ed-9513-48f8-f1ef-0c1b63347624"
      },
      "source": [
        "# Take a look at ratings_df\n",
        "ratings_df.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>userId</th>\n",
              "      <th>movieId</th>\n",
              "      <th>rating</th>\n",
              "      <th>timestamp</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>4.0</td>\n",
              "      <td>964982703</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>4.0</td>\n",
              "      <td>964981247</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1</td>\n",
              "      <td>6</td>\n",
              "      <td>4.0</td>\n",
              "      <td>964982224</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1</td>\n",
              "      <td>47</td>\n",
              "      <td>5.0</td>\n",
              "      <td>964983815</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1</td>\n",
              "      <td>50</td>\n",
              "      <td>5.0</td>\n",
              "      <td>964982931</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   userId  movieId  rating  timestamp\n",
              "0       1        1     4.0  964982703\n",
              "1       1        3     4.0  964981247\n",
              "2       1        6     4.0  964982224\n",
              "3       1       47     5.0  964983815\n",
              "4       1       50     5.0  964982931"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2TUaWt96k0q7",
        "outputId": "afd13baa-d03e-40c9-9dcf-f8c4cbda08d0"
      },
      "source": [
        "# Movie ID to movie name mapping\n",
        "movie_names = movies_df.set_index('movieId')['title'].to_dict()\n",
        "n_users = len(ratings_df.userId.unique())\n",
        "n_items = len(ratings_df.movieId.unique())\n",
        "print(\"Number of unique users:\", n_users)\n",
        "print(\"Number of unique movies:\", n_items)\n",
        "print(\"The full rating matrix will have:\", n_users*n_items, 'elements.')\n",
        "print('----------')\n",
        "print(\"Number of ratings:\", len(ratings_df))\n",
        "print(\"Therefore: \", len(ratings_df) / (n_users*n_items) * 100, '% of the matrix is filled.')\n",
        "print(\"We have an incredibly sparse matrix to work with here.\")\n",
        "print(\"And... as you can imagine, as the number of users and products grow, the number of elements will increase by n*2\")\n",
        "print(\"You are going to need a lot of memory to work with global scale... storing a full matrix in memory would be a challenge.\")\n",
        "print(\"One advantage here is that matrix factorization can realize the rating matrix implicitly, thus we don't need all the data\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Number of unique users: 610\n",
            "Number of unique movies: 9724\n",
            "The full rating matrix will have: 5931640 elements.\n",
            "----------\n",
            "Number of ratings: 100836\n",
            "Therefore:  1.6999683055613624 % of the matrix is filled.\n",
            "We have an incredibly sparse matrix to work with here.\n",
            "And... as you can imagine, as the number of users and products grow, the number of elements will increase by n*2\n",
            "You are going to need a lot of memory to work with global scale... storing a full matrix in memory would be a challenge.\n",
            "One advantage here is that matrix factorization can realize the rating matrix implicitly, thus we don't need all the data\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YnkTvMsCk0tY"
      },
      "source": [
        "import torch\n",
        "import numpy as np\n",
        "from torch.autograd import Variable\n",
        "from tqdm import tqdm_notebook as tqdm\n",
        "\n",
        "class MatrixFactorization(torch.nn.Module):\n",
        "    def __init__(self, n_users, n_items, n_factors=20):\n",
        "        super().__init__()\n",
        "        # create user embeddings\n",
        "        self.user_factors = torch.nn.Embedding(n_users, n_factors) # think of this as a lookup table for the input.\n",
        "        # create item embeddings\n",
        "        self.item_factors = torch.nn.Embedding(n_items, n_factors) # think of this as a lookup table for the input.\n",
        "        self.user_factors.weight.data.uniform_(0, 0.05)\n",
        "        self.item_factors.weight.data.uniform_(0, 0.05)\n",
        "        \n",
        "    def forward(self, data):\n",
        "        # matrix multiplication\n",
        "        users, items = data[:,0], data[:,1]\n",
        "        return (self.user_factors(users)*self.item_factors(items)).sum(1)\n",
        "    # def forward(self, user, item):\n",
        "    # \t# matrix multiplication\n",
        "    #     return (self.user_factors(user)*self.item_factors(item)).sum(1)\n",
        "    \n",
        "    def predict(self, user, item):\n",
        "        return self.forward(user, item)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "LTlGvz7sk0v2"
      },
      "source": [
        "# Creating the dataloader (necessary for PyTorch)\n",
        "from torch.utils.data.dataset import Dataset\n",
        "from torch.utils.data import DataLoader # package that helps transform your data to machine learning readiness\n",
        "\n",
        "# Note: This isn't 'good' practice, in a MLops sense but we'll roll with this since the data is already loaded in memory.\n",
        "class Loader(Dataset):\n",
        "    def __init__(self):\n",
        "        self.ratings = ratings_df.copy()\n",
        "        \n",
        "        # Extract all user IDs and movie IDs\n",
        "        users = ratings_df.userId.unique()\n",
        "        movies = ratings_df.movieId.unique()\n",
        "        \n",
        "        #--- Producing new continuous IDs for users and movies ---\n",
        "        \n",
        "        # Unique values : index\n",
        "        self.userid2idx = {o:i for i,o in enumerate(users)}\n",
        "        self.movieid2idx = {o:i for i,o in enumerate(movies)}\n",
        "        \n",
        "        # Obtained continuous ID for users and movies\n",
        "        self.idx2userid = {i:o for o,i in self.userid2idx.items()}\n",
        "        self.idx2movieid = {i:o for o,i in self.movieid2idx.items()}\n",
        "        \n",
        "        # return the id from the indexed values as noted in the lambda function down below.\n",
        "        self.ratings.movieId = ratings_df.movieId.apply(lambda x: self.movieid2idx[x])\n",
        "        self.ratings.userId = ratings_df.userId.apply(lambda x: self.userid2idx[x])\n",
        "        \n",
        "        \n",
        "        self.x = self.ratings.drop(['rating', 'timestamp'], axis=1).values\n",
        "        self.y = self.ratings['rating'].values\n",
        "        self.x, self.y = torch.tensor(self.x), torch.tensor(self.y) # Transforms the data to tensors (ready for torch models.)\n",
        "\n",
        "    def __getitem__(self, index):\n",
        "        return (self.x[index], self.y[index])\n",
        "\n",
        "    def __len__(self):\n",
        "        return len(self.ratings)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "J6MK3Ymmk0yi",
        "outputId": "50e960e6-ccc7-4852-98cf-55144f7848c7"
      },
      "source": [
        "num_epochs = 128\n",
        "cuda = torch.cuda.is_available()\n",
        "\n",
        "print(\"Is running on GPU:\", cuda)\n",
        "\n",
        "model = MatrixFactorization(n_users, n_items, n_factors=8)\n",
        "print(model)\n",
        "for name, param in model.named_parameters():\n",
        "    if param.requires_grad:\n",
        "        print(name, param.data)\n",
        "# GPU enable if you have a GPU...\n",
        "if cuda:\n",
        "    model = model.cuda()\n",
        "\n",
        "# MSE loss\n",
        "loss_fn = torch.nn.MSELoss()\n",
        "\n",
        "# ADAM optimizier\n",
        "optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)\n",
        "\n",
        "# Train data\n",
        "train_set = Loader()\n",
        "train_loader = DataLoader(train_set, 128, shuffle=True)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Is running on GPU: True\n",
            "MatrixFactorization(\n",
            "  (user_factors): Embedding(610, 8)\n",
            "  (item_factors): Embedding(9724, 8)\n",
            ")\n",
            "user_factors.weight tensor([[0.0030, 0.0149, 0.0045,  ..., 0.0316, 0.0093, 0.0484],\n",
            "        [0.0391, 0.0295, 0.0077,  ..., 0.0061, 0.0093, 0.0233],\n",
            "        [0.0094, 0.0131, 0.0115,  ..., 0.0347, 0.0217, 0.0316],\n",
            "        ...,\n",
            "        [0.0418, 0.0289, 0.0364,  ..., 0.0296, 0.0182, 0.0390],\n",
            "        [0.0333, 0.0219, 0.0277,  ..., 0.0402, 0.0059, 0.0311],\n",
            "        [0.0060, 0.0420, 0.0384,  ..., 0.0252, 0.0261, 0.0160]])\n",
            "item_factors.weight tensor([[0.0339, 0.0125, 0.0496,  ..., 0.0038, 0.0500, 0.0406],\n",
            "        [0.0438, 0.0302, 0.0096,  ..., 0.0058, 0.0257, 0.0467],\n",
            "        [0.0105, 0.0372, 0.0088,  ..., 0.0482, 0.0272, 0.0408],\n",
            "        ...,\n",
            "        [0.0173, 0.0326, 0.0255,  ..., 0.0412, 0.0301, 0.0379],\n",
            "        [0.0374, 0.0421, 0.0254,  ..., 0.0204, 0.0251, 0.0022],\n",
            "        [0.0212, 0.0367, 0.0220,  ..., 0.0069, 0.0263, 0.0371]])\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000,
          "referenced_widgets": [
            "3c1765cabeaf4d75a130311ddc4591a1",
            "6db170b52f5a4f72afd083a3a9c157aa",
            "69073fd458234bba829af9731b4fce1c",
            "88151edb53134487b95f6bcbcd7fd2b4",
            "9b185906b1dc465e93b9f058a1fec47a",
            "20b4738815cd467dba2946031d6d9027",
            "c279f9a0a0fe498b9db167a237517e6e",
            "005a499c40bd407ca20c2492d9c4f170"
          ]
        },
        "id": "8fIDIdStk000",
        "outputId": "84caf390-d372-4d82-a045-cbf12a9c8cce"
      },
      "source": [
        "for it in tqdm(range(num_epochs)):\n",
        "    losses = []\n",
        "    for x, y in train_loader:\n",
        "         if cuda:\n",
        "            x, y = x.cuda(), y.cuda()\n",
        "            optimizer.zero_grad()\n",
        "            outputs = model(x)\n",
        "            loss = loss_fn(outputs.squeeze(), y.type(torch.float32))\n",
        "            losses.append(loss.item())\n",
        "            loss.backward()\n",
        "            optimizer.step()\n",
        "    print(\"iter #{}\".format(it), \"Loss:\", sum(losses) / len(losses))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/ipykernel_launcher.py:1: TqdmDeprecationWarning: This function will be removed in tqdm==5.0.0\n",
            "Please use `tqdm.notebook.tqdm` instead of `tqdm.tqdm_notebook`\n",
            "  \"\"\"Entry point for launching an IPython kernel.\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "display_data",
          "data": {
            "application/vnd.jupyter.widget-view+json": {
              "model_id": "3c1765cabeaf4d75a130311ddc4591a1",
              "version_minor": 0,
              "version_major": 2
            },
            "text/plain": [
              "HBox(children=(FloatProgress(value=0.0, max=128.0), HTML(value='')))"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "stream",
          "text": [
            "iter #0 Loss: 11.064539746584625\n",
            "iter #1 Loss: 4.749444664734875\n",
            "iter #2 Loss: 2.4776223112786484\n",
            "iter #3 Loss: 1.72177541634153\n",
            "iter #4 Loss: 1.3460204232919035\n",
            "iter #5 Loss: 1.1284338527827094\n",
            "iter #6 Loss: 0.9915084930392086\n",
            "iter #7 Loss: 0.9002359872542057\n",
            "iter #8 Loss: 0.8372054895395555\n",
            "iter #9 Loss: 0.7921712103909647\n",
            "iter #10 Loss: 0.7592169020306035\n",
            "iter #11 Loss: 0.734483423155879\n",
            "iter #12 Loss: 0.7160191048825453\n",
            "iter #13 Loss: 0.7014374917912\n",
            "iter #14 Loss: 0.690310317020731\n",
            "iter #15 Loss: 0.6816033662348835\n",
            "iter #16 Loss: 0.6750705706589113\n",
            "iter #17 Loss: 0.669739288727039\n",
            "iter #18 Loss: 0.6658609225816533\n",
            "iter #19 Loss: 0.6628223651935001\n",
            "iter #20 Loss: 0.6604955623370742\n",
            "iter #21 Loss: 0.6587029967059944\n",
            "iter #22 Loss: 0.6573294878459824\n",
            "iter #23 Loss: 0.6564567382565609\n",
            "iter #24 Loss: 0.6555627360183576\n",
            "iter #25 Loss: 0.6549196255388599\n",
            "iter #26 Loss: 0.6539314403978701\n",
            "iter #27 Loss: 0.6528688056517373\n",
            "iter #28 Loss: 0.6521614116006696\n",
            "iter #29 Loss: 0.6506869314890827\n",
            "iter #30 Loss: 0.6492639796307245\n",
            "iter #31 Loss: 0.6471106028420671\n",
            "iter #32 Loss: 0.645041638408518\n",
            "iter #33 Loss: 0.6422005586212661\n",
            "iter #34 Loss: 0.638611158819368\n",
            "iter #35 Loss: 0.6344703135983593\n",
            "iter #36 Loss: 0.6294693703276252\n",
            "iter #37 Loss: 0.6236191429765091\n",
            "iter #38 Loss: 0.6167608291894047\n",
            "iter #39 Loss: 0.6090864502839025\n",
            "iter #40 Loss: 0.6006192625854826\n",
            "iter #41 Loss: 0.591128448733521\n",
            "iter #42 Loss: 0.5818279621942999\n",
            "iter #43 Loss: 0.5720471330932554\n",
            "iter #44 Loss: 0.5620070278342\n",
            "iter #45 Loss: 0.5522127401859022\n",
            "iter #46 Loss: 0.5425238067728614\n",
            "iter #47 Loss: 0.5330987115045489\n",
            "iter #48 Loss: 0.5237701579852758\n",
            "iter #49 Loss: 0.5146918527895424\n",
            "iter #50 Loss: 0.5060733147532807\n",
            "iter #51 Loss: 0.49774435866000083\n",
            "iter #52 Loss: 0.4898831197226108\n",
            "iter #53 Loss: 0.48233551210558356\n",
            "iter #54 Loss: 0.47518290367525845\n",
            "iter #55 Loss: 0.4683648519936552\n",
            "iter #56 Loss: 0.4619765629623142\n",
            "iter #57 Loss: 0.45608887344901333\n",
            "iter #58 Loss: 0.4503257277464201\n",
            "iter #59 Loss: 0.4448733877220432\n",
            "iter #60 Loss: 0.4392992372288922\n",
            "iter #61 Loss: 0.43464641615294564\n",
            "iter #62 Loss: 0.42979167560635484\n",
            "iter #63 Loss: 0.4254226601365859\n",
            "iter #64 Loss: 0.4212072497318844\n",
            "iter #65 Loss: 0.41702721674505827\n",
            "iter #66 Loss: 0.41309558013974107\n",
            "iter #67 Loss: 0.4096982266735002\n",
            "iter #68 Loss: 0.4059119510469098\n",
            "iter #69 Loss: 0.40268489101967836\n",
            "iter #70 Loss: 0.39933304133148967\n",
            "iter #71 Loss: 0.3963695630468995\n",
            "iter #72 Loss: 0.3934276655959296\n",
            "iter #73 Loss: 0.39076741312058444\n",
            "iter #74 Loss: 0.38803952179735685\n",
            "iter #75 Loss: 0.38546007302433705\n",
            "iter #76 Loss: 0.3831277103328765\n",
            "iter #77 Loss: 0.3808427186030422\n",
            "iter #78 Loss: 0.3784061186015606\n",
            "iter #79 Loss: 0.376466433446722\n",
            "iter #80 Loss: 0.3743195962822679\n",
            "iter #81 Loss: 0.37235598676473963\n",
            "iter #82 Loss: 0.3705784824066961\n",
            "iter #83 Loss: 0.36864257153823293\n",
            "iter #84 Loss: 0.36688284131551757\n",
            "iter #85 Loss: 0.365231491625309\n",
            "iter #86 Loss: 0.363480249164522\n",
            "iter #87 Loss: 0.36211012859786224\n",
            "iter #88 Loss: 0.3606044158036939\n",
            "iter #89 Loss: 0.3591318737696573\n",
            "iter #90 Loss: 0.35775118635088055\n",
            "iter #91 Loss: 0.35647212154217783\n",
            "iter #92 Loss: 0.35528279884439434\n",
            "iter #93 Loss: 0.3539668278494462\n",
            "iter #94 Loss: 0.3529103894902365\n",
            "iter #95 Loss: 0.35162870211498387\n",
            "iter #96 Loss: 0.3504359047424975\n",
            "iter #97 Loss: 0.3495060858614554\n",
            "iter #98 Loss: 0.34839825456971446\n",
            "iter #99 Loss: 0.3474773046782779\n",
            "iter #100 Loss: 0.34632887125847306\n",
            "iter #101 Loss: 0.3455469298937599\n",
            "iter #102 Loss: 0.34439465970859917\n",
            "iter #103 Loss: 0.34378151434856624\n",
            "iter #104 Loss: 0.342845733244407\n",
            "iter #105 Loss: 0.3420450622924996\n",
            "iter #106 Loss: 0.3412834131891655\n",
            "iter #107 Loss: 0.3402374327031489\n",
            "iter #108 Loss: 0.3397955849653271\n",
            "iter #109 Loss: 0.3387879188063786\n",
            "iter #110 Loss: 0.33817208227394197\n",
            "iter #111 Loss: 0.33761035310586696\n",
            "iter #112 Loss: 0.3367398034043724\n",
            "iter #113 Loss: 0.3361376861895099\n",
            "iter #114 Loss: 0.335421702375418\n",
            "iter #115 Loss: 0.3348476519325966\n",
            "iter #116 Loss: 0.33413760375401697\n",
            "iter #117 Loss: 0.3337071446635699\n",
            "iter #118 Loss: 0.3331990203805986\n",
            "iter #119 Loss: 0.3324130240846709\n",
            "iter #120 Loss: 0.33211925737370696\n",
            "iter #121 Loss: 0.3313073167757032\n",
            "iter #122 Loss: 0.33095684267467046\n",
            "iter #123 Loss: 0.3304014680954406\n",
            "iter #124 Loss: 0.3297704937229604\n",
            "iter #125 Loss: 0.3293193760446183\n",
            "iter #126 Loss: 0.32888494188032175\n",
            "iter #127 Loss: 0.32834809857803554\n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zs_GVbSYmhib",
        "outputId": "d4a5a7f6-f2a6-4d08-9083-84a2812c3f45"
      },
      "source": [
        "# By training the model, we will have tuned latent factors for movies and users.\n",
        "c = 0\n",
        "uw = 0\n",
        "iw = 0 \n",
        "for name, param in model.named_parameters():\n",
        "    if param.requires_grad:\n",
        "        print(name, param.data)\n",
        "        if c == 0:\n",
        "          uw = param.data\n",
        "          c +=1\n",
        "        else:\n",
        "          iw = param.data\n",
        "        #print('param_data', param_data)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "user_factors.weight tensor([[ 0.6636,  1.7670,  1.5851,  ...,  1.5591,  0.9846,  1.3279],\n",
            "        [ 0.2886,  0.8389,  0.4740,  ...,  0.0211,  1.7432,  1.8250],\n",
            "        [-0.1276,  0.3505, -1.8636,  ..., -1.8244,  2.3191,  2.1920],\n",
            "        ...,\n",
            "        [ 1.5623,  0.0149,  0.6837,  ...,  2.2128,  1.5504, -0.0838],\n",
            "        [ 0.8281,  0.7045,  0.6922,  ...,  1.0350,  0.5839,  1.2660],\n",
            "        [ 0.8088,  1.1780,  0.7822,  ...,  0.9027,  2.0788,  1.3200]],\n",
            "       device='cuda:0')\n",
            "item_factors.weight tensor([[ 0.4925,  0.3693,  0.7865,  ...,  0.1419,  0.4939,  0.3609],\n",
            "        [ 0.1813,  0.2992,  0.4251,  ...,  0.5503, -0.0829,  0.6948],\n",
            "        [ 0.5640,  0.3030,  0.5318,  ...,  0.5683,  0.7503,  0.3950],\n",
            "        ...,\n",
            "        [ 0.3246,  0.3380,  0.3319,  ...,  0.3477,  0.3367,  0.3458],\n",
            "        [ 0.3952,  0.4012,  0.3834,  ...,  0.3810,  0.3876,  0.3640],\n",
            "        [ 0.4014,  0.4191,  0.4042,  ...,  0.3881,  0.4108,  0.4209]],\n",
            "       device='cuda:0')\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IJgie01_p8k5"
      },
      "source": [
        "trained_movie_embeddings = model.item_factors.weight.data.cpu().numpy()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "R-_tHZ_E_rub",
        "outputId": "cb97ce5d-7140-43fa-8ffa-7603a22eee2c"
      },
      "source": [
        "len(trained_movie_embeddings) # unique movie factor weights"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "9724"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 30
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bl9s4iqXy75q"
      },
      "source": [
        "from sklearn.cluster import KMeans\n",
        "# Fit the clusters based on the movie weights\n",
        "kmeans = KMeans(n_clusters=10, random_state=0).fit(trained_movie_embeddings)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8MDzp-9u-m5n",
        "outputId": "c6f77e4d-68d1-49c5-c022-25e80e99007d"
      },
      "source": [
        "'''It can be seen here that the movies that are in the same cluster tend to have\n",
        "similar genres. Also note that the algorithm is unfamiliar with the movie name\n",
        "and only obtained the relationships by looking at the numbers representing how\n",
        "users have responded to the movie selections.'''\n",
        "for cluster in range(10):\n",
        "  print(\"Cluster #{}\".format(cluster))\n",
        "  movs = []\n",
        "  for movidx in np.where(kmeans.labels_ == cluster)[0]:\n",
        "    movid = train_set.idx2movieid[movidx]\n",
        "    rat_count = ratings_df.loc[ratings_df['movieId']==movid].count()[0]\n",
        "    movs.append((movie_names[movid], rat_count))\n",
        "  for mov in sorted(movs, key=lambda tup: tup[1], reverse=True)[:10]:\n",
        "    print(\"\\t\", mov[0])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Cluster #0\n",
            "\t Forrest Gump (1994)\n",
            "\t Shawshank Redemption, The (1994)\n",
            "\t Silence of the Lambs, The (1991)\n",
            "\t Matrix, The (1999)\n",
            "\t Star Wars: Episode IV - A New Hope (1977)\n",
            "\t Terminator 2: Judgment Day (1991)\n",
            "\t Star Wars: Episode V - The Empire Strikes Back (1980)\n",
            "\t Usual Suspects, The (1995)\n",
            "\t Raiders of the Lost Ark (Indiana Jones and the Raiders of the Lost Ark) (1981)\n",
            "\t Lord of the Rings: The Fellowship of the Ring, The (2001)\n",
            "Cluster #1\n",
            "\t Godzilla (1998)\n",
            "\t Super Mario Bros. (1993)\n",
            "\t Honey, I Blew Up the Kid (1992)\n",
            "\t Battlefield Earth (2000)\n",
            "\t Mighty Morphin Power Rangers: The Movie (1995)\n",
            "\t Superman IV: The Quest for Peace (1987)\n",
            "\t Next Karate Kid, The (1994)\n",
            "\t Volcano (1997)\n",
            "\t Karate Kid, Part III, The (1989)\n",
            "\t Rambo III (1988)\n",
            "Cluster #2\n",
            "\t Alien (1979)\n",
            "\t Die Hard (1988)\n",
            "\t Groundhog Day (1993)\n",
            "\t Terminator, The (1984)\n",
            "\t Aliens (1986)\n",
            "\t Austin Powers: The Spy Who Shagged Me (1999)\n",
            "\t Clerks (1994)\n",
            "\t American Pie (1999)\n",
            "\t Heat (1995)\n",
            "\t Austin Powers: International Man of Mystery (1997)\n",
            "Cluster #3\n",
            "\t Jurassic Park (1993)\n",
            "\t Apollo 13 (1995)\n",
            "\t Fugitive, The (1993)\n",
            "\t Batman (1989)\n",
            "\t Sixth Sense, The (1999)\n",
            "\t True Lies (1994)\n",
            "\t Back to the Future (1985)\n",
            "\t Men in Black (a.k.a. MIB) (1997)\n",
            "\t Ace Ventura: Pet Detective (1994)\n",
            "\t Mask, The (1994)\n",
            "Cluster #4\n",
            "\t Batman Forever (1995)\n",
            "\t Net, The (1995)\n",
            "\t Clueless (1995)\n",
            "\t Cliffhanger (1993)\n",
            "\t Broken Arrow (1996)\n",
            "\t Contact (1997)\n",
            "\t Nutty Professor, The (1996)\n",
            "\t Demolition Man (1993)\n",
            "\t Face/Off (1997)\n",
            "\t Liar Liar (1997)\n",
            "Cluster #5\n",
            "\t Independence Day (a.k.a. ID4) (1996)\n",
            "\t Speed (1994)\n",
            "\t Mission: Impossible (1996)\n",
            "\t Star Wars: Episode I - The Phantom Menace (1999)\n",
            "\t Titanic (1997)\n",
            "\t Twister (1996)\n",
            "\t Star Trek: Generations (1994)\n",
            "\t Crimson Tide (1995)\n",
            "\t Armageddon (1998)\n",
            "\t Star Wars: Episode II - Attack of the Clones (2002)\n",
            "Cluster #6\n",
            "\t Waterworld (1995)\n",
            "\t Avatar (2009)\n",
            "\t 300 (2007)\n",
            "\t Unbreakable (2000)\n",
            "\t Pirates of the Caribbean: Dead Man's Chest (2006)\n",
            "\t Bridget Jones's Diary (2001)\n",
            "\t Juno (2007)\n",
            "\t Animal House (1978)\n",
            "\t Piano, The (1993)\n",
            "\t Gone in 60 Seconds (2000)\n",
            "Cluster #7\n",
            "\t Braveheart (1995)\n",
            "\t Shrek (2001)\n",
            "\t Dances with Wolves (1990)\n",
            "\t Incredibles, The (2004)\n",
            "\t Willy Wonka & the Chocolate Factory (1971)\n",
            "\t Batman Begins (2005)\n",
            "\t 2001: A Space Odyssey (1968)\n",
            "\t Harry Potter and the Sorcerer's Stone (a.k.a. Harry Potter and the Philosopher's Stone) (2001)\n",
            "\t Harry Potter and the Chamber of Secrets (2002)\n",
            "\t As Good as It Gets (1997)\n",
            "Cluster #8\n",
            "\t Schindler's List (1993)\n",
            "\t Toy Story (1995)\n",
            "\t Aladdin (1992)\n",
            "\t Lion King, The (1994)\n",
            "\t Babe (1995)\n",
            "\t E.T. the Extra-Terrestrial (1982)\n",
            "\t Ghost (1990)\n",
            "\t Breakfast Club, The (1985)\n",
            "\t Up (2009)\n",
            "\t Four Weddings and a Funeral (1994)\n",
            "Cluster #9\n",
            "\t Pulp Fiction (1994)\n",
            "\t Fight Club (1999)\n",
            "\t American Beauty (1999)\n",
            "\t Seven (a.k.a. Se7en) (1995)\n",
            "\t Godfather, The (1972)\n",
            "\t Fargo (1996)\n",
            "\t Twelve Monkeys (a.k.a. 12 Monkeys) (1995)\n",
            "\t Memento (2000)\n",
            "\t Monty Python and the Holy Grail (1975)\n",
            "\t One Flew Over the Cuckoo's Nest (1975)\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
