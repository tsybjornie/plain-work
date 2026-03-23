import os
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class AutonomousKiloClaw:
    def __init__(self):
        """
        The Zero-Touch Business Manager.
        This AI reads business state and decides what to do next without asking you.
        """
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.api_key)
        
    def evaluate_business_state(self):
        """
        Simulates gathering data from your business APIs (Stripe balance, TikTok views, etc)
        """
        # MOCK DATA: In a real environment, this pulls live via Stripe & Social APIs
        business_state = {
            "current_time": time.strftime('%Y-%m-%d %H:%M:%S'),
            "stripe_daily_revenue": 1479.0, # They sold some sample boxes
            "tiktok_views_last_24h": 4500,  # Views are dropping
            "pending_site_assessments": 2
        }
        return business_state
        
    def make_executive_decision(self, state):
        """
        Forces the LLM to choose the most profitable next action.
        """
        print("\n[KiloClaw] Analyzing Business State...")
        prompt = f"""
        You are KiloClaw, the autonomous CEO of Plainwork (a Mineral Surface Studio). 
        Your goal is S$2.2M monthly net profit. 
        
        Current State:
        - Revenue Today: S${state['stripe_daily_revenue']}
        - Social Views: {state['tiktok_views_last_24h']}
        - Pending Site Visits: {state['pending_site_assessments']}
        
        You have 3 possible actions you can trigger right now:
        1. "GENERATE_VIRAL_VIDEO" - If views are under 10,000, trigger Runway/HeyGen.
        2. "EXECUTE_B2B_OUTREACH" - If revenue is under S$5,000, scrape Qanvast and pitch 5 Interior Designers.
        3. "WAIT" - If numbers are high, do nothing and save API costs.
        
        Reply ONLY with the exact action string. No explanation.
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": prompt}],
            temperature=0.0
        )
        
        decision = response.choices[0].message.content.strip()
        print(f"-> Decision Made: {decision}")
        return decision
        
    def execute_action(self, decision):
        """
        Routes the decision to the actual Python scripts we've already built.
        """
        if decision == "GENERATE_VIRAL_VIDEO":
            print("[KiloClaw] Executing: Triggering runway_heygen_live.py to boost views...")
            # In production: subprocess.run(["python3", "runway_heygen_live.py"])
            print("-> Successfully triggered new video batch.")
            
        elif decision == "EXECUTE_B2B_OUTREACH":
            print("[KiloClaw] Executing: Triggering auto_outreach_bot.py to secure commercial revenue...")
            # In production: subprocess.run(["python3", "auto_outreach_bot.py"])
            print("-> Successfully dispatched 5 DMs to Interior Designers.")
            
        else:
            print("[KiloClaw] Maintaining holding pattern. Conserving resources.")

if __name__ == "__main__":
    agent = AutonomousKiloClaw()
    current_state = agent.evaluate_business_state()
    next_move = agent.make_executive_decision(current_state)
    agent.execute_action(next_move)
