# Transformer完整输入输出流程演示

import numpy as np

class TransformerIODemo:
    def __init__(self):
        # 简化的词汇表
        self.vocab = {
            "<BOS>": 0,    # Beginning of sequence
            "I": 1,
            "am": 2, 
            "a": 3,
            "transformer": 4,
            ".": 5,
            "<EOS>": 6     # End of sequence
        }
        self.id_to_token = {v: k for k, v in self.vocab.items()}
        self.vocab_size = len(self.vocab)
    
    def tokenize(self, text):
        """简化的tokenization"""
        # 在实际中，这会是复杂的BPE过程
        tokens = text.split()
        token_ids = [self.vocab.get(token, self.vocab["<EOS>"]) for token in tokens]
        return [self.vocab["<BOS>"]] + token_ids  # 添加BOS token
    
    def simulate_transformer_forward(self, token_ids):
        """模拟transformer的前向传播"""
        seq_len = len(token_ids)
        
        # 模拟输出logits [seq_len, vocab_size]
        # 在真实情况下，这些是通过复杂的注意力和MLP层计算的
        logits = np.random.randn(seq_len, self.vocab_size)
        
        # 手动设置一些合理的logits来展示概念
        for i in range(seq_len):
            if i == 1:  # 预测"am"
                logits[i, self.vocab["am"]] = 3.0
            elif i == 2:  # 预测"a" 
                logits[i, self.vocab["a"]] = 2.5
            elif i == 3:  # 预测"transformer"
                logits[i, self.vocab["transformer"]] = 4.0
            elif i == 4:  # 预测"."
                logits[i, self.vocab["."]] = 2.0
        
        return logits
    
    def logits_to_probabilities(self, logits):
        """将logits转换为概率"""
        def softmax(x):
            exp_x = np.exp(x - np.max(x))
            return exp_x / np.sum(exp_x)
        
        probabilities = np.array([softmax(logit_row) for logit_row in logits])
        return probabilities
    
    def demonstrate_causal_attention(self, seq_len):
        """演示因果注意力掩码"""
        print("=== 因果注意力掩码 ===")
        mask = np.tril(np.ones((seq_len, seq_len)))
        print("掩码矩阵 (1=可见, 0=不可见):")
        print("   ", " ".join([f"{i:2}" for i in range(seq_len)]))
        for i in range(seq_len):
            row = " ".join([f"{int(mask[i,j]):2}" for j in range(seq_len)])
            print(f"{i}: {row}")
        return mask
    
    def run_complete_demo(self):
        """运行完整演示"""
        print("=" * 50)
        print("TRANSFORMER 输入输出完整流程演示")
        print("=" * 50)
        
        # 步骤1: 文本输入
        input_text = "I am a transformer"
        print(f"\n1. 输入文本: '{input_text}'")
        
        # 步骤2: Tokenization
        token_ids = self.tokenize(input_text)
        tokens = [self.id_to_token[id] for id in token_ids]
        print(f"\n2. Tokenization:")
        print(f"   Tokens: {tokens}")
        print(f"   Token IDs: {token_ids}")
        print(f"   序列长度: {len(token_ids)}")
        
        # 步骤3: 演示因果注意力
        print(f"\n3. 因果注意力:")
        self.demonstrate_causal_attention(len(token_ids))
        
        # 步骤4: 模拟前向传播
        print(f"\n4. Transformer前向传播:")
        logits = self.simulate_transformer_forward(token_ids)
        print(f"   输出形状: {logits.shape}")
        print(f"   含义: [{len(token_ids)} 位置] x [{self.vocab_size} 词汇表大小]")
        
        # 步骤5: 转换为概率
        print(f"\n5. Logits -> 概率分布:")
        probabilities = self.logits_to_probabilities(logits)
        
        # 展示每个位置的预测
        print(f"\n6. 每个位置的预测:")
        for i in range(len(tokens)):
            current_token = tokens[i]
            
            # 找到概率最高的下一个token
            next_token_probs = probabilities[i]
            best_next_id = np.argmax(next_token_probs)
            best_next_token = self.id_to_token[best_next_id]
            best_prob = next_token_probs[best_next_id]
            
            print(f"   位置{i} '{current_token}' -> 预测: '{best_next_token}' (概率: {best_prob:.3f})")
            
            # 显示top 3预测
            top3_ids = np.argsort(next_token_probs)[-3:][::-1]
            top3_info = [(self.id_to_token[id], next_token_probs[id]) for id in top3_ids]
            print(f"      Top 3: {top3_info}")
        
        # 步骤7: 文本生成示例
        print(f"\n7. 文本生成过程:")
        self.demonstrate_text_generation()
    
    def demonstrate_text_generation(self):
        """演示文本生成过程"""
        current_text = "I am"
        print(f"   起始: '{current_text}'")
        
        for step in range(3):
            print(f"   步骤 {step+1}:")
            
            # 模拟获取下一个token
            if step == 0:
                next_token = "a"
                prob = 0.85
            elif step == 1:
                next_token = "transformer"
                prob = 0.92
            else:
                next_token = "."
                prob = 0.78
            
            current_text += " " + next_token
            print(f"     输入: '{current_text[:-len(next_token)-1]}'")
            print(f"     预测: '{next_token}' (概率: {prob})")
            print(f"     新文本: '{current_text}'")

# 运行演示
demo = TransformerIODemo()
demo.run_complete_demo()

print("\n" + "=" * 50)
print("关键要点总结:")
print("=" * 50)
key_points = [
    "1. 文本通过tokenization转换为数字序列",
    "2. Transformer为每个位置输出整个词汇表的logits",
    "3. 因果掩码确保每个位置只能看到之前的token",
    "4. Softmax将logits转换为有效的概率分布", 
    "5. 文本生成是自回归的：一次生成一个token",
    "6. 每个新token都需要重新通过模型获得下一个预测"
]

for point in key_points:
    print(point)