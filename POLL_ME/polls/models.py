from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Poll(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    text=models.CharField(max_length=255)
    pub_date=models.DateField() 
    
    def user_can_vote(self,user):
        user_votes=user.vote_set.all()
        
        for vote in user_votes:
            if vote.poll==self:
                return False;
        return True   
    @property
    def num_votes(self):
        return self.vote_set.count()    
    def __str__(self):
        return self.text    
    def get_results_dict(self):
        res=[]
        for choice in self.choice_set.all():
            d={}
            d['text']=choice.choice_text
            d['num_votes']=choice.num_votes
            if self.num_votes==0:
                d['percentage']=0
            else:
                d['percentage']=choice.num_votes/self.num_votes*100
            res.append(d)
        return res            

class Choice(models.Model):
    poll=models.ForeignKey(Poll,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=255)
    def __str__(self):
        return '{}-{}'.format(self.poll.text[:25],self.choice_text[:25])   
    @property
    def num_votes(self):
        return self.vote_set.count()       
 
class Vote(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    poll=models.ForeignKey(Poll,on_delete=models.CASCADE)
    choice=models.ForeignKey(Choice,on_delete=models.CASCADE)   
    def __str__(self):
        return '{}-{}'.format(self.user,self.choice)     
        
