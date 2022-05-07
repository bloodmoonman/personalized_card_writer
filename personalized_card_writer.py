from contextlib import contextmanager

class Personalized():
  def __init__(self, sender_name, recipient):
    self.sender_name = sender_name
    self.recipient = recipient
    self.file = open(f'{self.sender_name}_personalized.txt', 'w')

  def __enter__(self):
    self.file.write(f'Dear {self.recipient},\n')
    return self.file

  def __exit__(self, *exc):
    self.file.write(f'Sincerely,\n{self.sender_name}')
    self.file.close()


with Personalized('Aykan', 'Seper') as personal_file:
  personal_file.write("I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.")











