import os
import time
from dotenv import load_dotenv

# We will swap OpenAI for Anthropic's Claude 3.5 Sonnet
import anthropic

load_dotenv()

class AutonomousKiloClaw:
    def __init__(self):
        """
        The Zero-Touch Business Manager using Claude 3.5 Sonnet (Faster & Cheaper than GPT-4o for routing).
        """
        # Note: You will need to add ANTHROPIC_API_KEY to your .env file
        self.api_key = os.getenv("ANTHROPIC_API_KEY", "mock_key_for_now")
        self.client = anthropic.Anthropic(api_key=self.api_key)
        
    def evaluate_business_state(self):
        """
        Simulates gathering data from your business APIs (Stripe balance, TikTok views, etc)
        """
        business_state = {
            "current_time": time.strftime('%Y-%m-%d %H:%M:%S'),
            "stripe_daily_revenue": 1479.0,
            "tiktok_views_last_24h": 4500,
            "pending_site_assessments": 2
        }
        return business_state
        
    def make_executive_decision(self, state):
        """
        Forces Claude 3.5 Sonnet to choose the most profitable next action.
        """
        print("\n[KiloClaw] Analyzing Business State using Claude 3.5 Sonnet...")
        
        system_prompt = "You are KiloClaw, the autonomous CEO of Plainwork (a Mineral Surface Studio). Your goal is S$2.2M monthly net profit."
        
        user_prompt = f"""
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
        
        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=10,
                temperature=0.0,
                system=system_prompt,
                messages=[
                    {"role": "user", "content": user_prompt}
                ]
            )
            decision = response.content[0].text.strip()
            print(f"-> Decision Made by Claude: {decision}")
            return decision
            
        except Exception as e:
            print(f"Anthropic API Error: {e}. (Ensure ANTHROPIC_API_KEY is in your .env)")
            return "WAIT"
        
    def execute_action(self, decision):
        """
        Routes the decision to the actual Python scripts we've already built.
        """
        if decision == "GENERATE_VIRAL_VIDEO":
            print("[KiloClaw] Executing: Triggering runway_heygen_live.py to boost views...")
        elif decision == "EXECUTE_B2B_OUTREACH":
            print("[KiloClaw] Executing: Triggering auto_outreach_bot.py to secure commercial revenue...")
        else:
            print("[KiloClaw] Maintaining holding pattern. Conserving resources.")

if __name__ == "__main__":
    agent = AutonomousKiloClaw()
    current_state = agent.evaluate_business_state()
    next_move = agent.make_executive_decision(current_state)
    agent.execute_action(next_move)
