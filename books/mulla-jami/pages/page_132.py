# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 132 (printed ١٣١)."""

PAGE_NUMBER = 132
PRINTED_PAGE = "١٣١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "(زيد قائم أبوه[[١]]). فهذا مثال لما أسند إليه شبه الفعل.",
     "en": "(“Zayd, standing is his father,” Zaydun qāʾimun abūhu). This is an example of that to which the verb-resembler is predicated."},
    {"type": "matn",
     "ar": "(والأصل في الفاعل[[٢]])، أي: ما ينبغي أن يكون الفاعل عليه[[٣]]، إن لم يمنع مانع",
     "en": "(And the rule (aṣl) regarding the agent) — that is, that upon which the agent ought to be, if no impediment prevents it —"},
    {"type": "matn",
     "ar": "(أن يلي[[٤]] الفعل) المسند إليه[[٥]]، أي: يكون بعده[[٦]] من غير أن يتقدم عليه شيء آخر من معمولاته؛",
     "en": "(is that it should immediately follow the verb) predicated of it — that is, that it come after it without anything else of the verb’s governed elements preceding it;"},
    {"type": "matn",
     "ar": "لأنه كالجزء من الفعل؛ لشدة احتياج الفعل إليه[[٧]]، ويدل على…",
     "en": "because it is as though it were a part of the verb, on account of the verb’s intense need of it; and it indicates…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "قيل: لو قال: «أبواه» بصيغة التثنية لكان نصا فيما قصده، فإن «أبوه» بصيغة المفرد يحتمل أن يكون مبتدأ قدم على خبره.",
     "en": "It is said: had he said “abawāhu” in the dual form, it would have been explicit as to what he intended; for “abūhu” in the singular form allows of being a mubtadaʾ placed before its predicate."},
    {"type": "pair",
     "ar": "ورد بأن احتمال كونه مبتدأ باطل، فإنه لو كان مبتدأ لوجب تقديمه على الخبر، كما في «زيد قائم»، فتأمل.",
     "en": "But this is answered: the possibility of its being a mubtadaʾ is void, for were it a mubtadaʾ its precedence over the predicate would be obligatory, as in “Zayd is standing (Zaydun qāʾim)” — so reflect."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يشير إلى أن اللام للعهد، أي: الأولى لحال الفاعل بالنظر إلى نفسه، فلذا فسر بقوله: أي: ينبغي إلى آخره.",
     "en": "He indicates that the definite article is one of specific reference — that is, what is most fitting for the state of the agent considered in itself; and for this reason he interpreted it by his words “that is, it ought…,” to the end."},
    {"type": "pair",
     "ar": "فالمراد بالانبغاء الأولوية الغير الواصلة إلى حد الوجوب؛ لأن الانبغاء يستعمل بمعنى اللزوم واللياقة.",
     "en": "What is meant by “ought” (inbighāʾ) is a preferability not reaching the degree of obligation; for “ought” is used in the sense of necessity and of fittingness."},
    {"type": "pair",
     "ar": "قال عبد الغفور: قوله: «في الفاعل» وكذا الأصل فيما هو بمعناه أي: يقرب من الفعل، ويتقدم على ما ليس بمعناه كالمفعول الأول من باب «أعطيت» بالنسبة إلى مفعوله الثاني، وكذا الحال في المفعول بلا واسطة بالقياس إلى المفعول بواسطة.",
     "en": "ʿAbd al-Ghafūr said: his words “regarding the agent” — likewise the rule holds for whatever is in its sense, namely that it be near the verb and precede what is not in its sense — like the first object of a verb of the “aʿṭaytu (I gave)” class relative to its second object; and so too the case of the direct object relative to the indirect (prepositional) object."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "الحاصل: أن الفاعل من حيث هو فاعل يقتضي قربه من الفعل ورجحانه، لكن قد يزول ذلك الاقتضاء بعارض يقتضي رجحان البعد أو وجوبه،",
     "en": "The upshot: the agent, in so far as it is an agent, requires its nearness to the verb and the preferability [of that]; but this requirement may lapse through some accidental factor requiring the preferability of distance, or its obligation."},
    {"type": "pair",
     "ar": "ونظير ذلك ما يقال: إن الماء بطبعه يقتضي البرودة، لكن قد يزول ذلك الاقتضاء بعارض مسخن.",
     "en": "A parallel is what is said: water by its nature requires coldness, yet this requirement may lapse through an accidental heating factor."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "هو في اللغة: ما يبنى عليه شيء. وفي العرف: القاعدة.",
     "en": "The aṣl (root/rule) is, in the language, that upon which a thing is built; and in [technical] usage: the general rule (al-qāʿida)."},
    {"type": "pair",
     "ar": "إن قلت: لم آثر هذه العبارة على قولك الأولى: «أن يلي» مع أنه أوضح وأحسن لمراعاة الاشتقاق؟",
     "en": "If you say: why did he prefer this expression [“the aṣl is…”] over your earlier phrase “that it immediately follow,” even though the latter is clearer and better for observing derivation?"},
    {"type": "pair",
     "ar": "قلنا: لأن في لفظ «الأصل» لمحا إلى قرب الفاعل من الفعل، كأنه بمنزلة قاعدة لا يجوز هدمها، وأنه ليس بمجرد أولويته، بل يبتنى عليه بعض الأحكام كما بينه بقوله: «فلذلك جاز إلى آخره»، ففيه زيادة تشويق إلى استماع الحكم الملقى.",
     "en": "We say: because in the word “aṣl” there is an allusion to the agent’s nearness to the verb, as though it were a foundation that may not be demolished, and [an indication] that it is not merely its being preferable, but rather certain rulings are built upon it — as he clarified by his words “and for that reason it is permitted…,” to the end. So in it is added incitement to attend to the ruling being conveyed."},
    {"type": "pair",
     "ar": "قال عبد الغفور: قوله: «أن يلي الفعل» لم يقل: أن يليه مع أنه أخصر وأشمل لشموله شبه الفعل أيضا، فوضع المظهر موضع المضمر لزيادة التمكن في الذهن والإشارة إلى أن الفعل أصل في هذا الحكم، وشبه الفعل ملحق به.",
     "en": "ʿAbd al-Ghafūr said: his words “that it immediately follow the verb” — he did not say “that it follow it,” even though the latter is more concise and more comprehensive, since it would include the verb-resembler too; but he set the overt noun in the place of the pronoun to give it greater fixity in the mind, and to indicate that the verb is the origin (aṣl) in this ruling, while the verb-resembler is annexed to it."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "يعني: اللام للعهد، وإنما قال: الأصل أن يلي الفعل، ولم يقل: أن يليه، فيرجع الضمير إلى أحد الأمرين، فيكون أخصر وأشمل لإبهام الأخصر وإيهامه أن الأصل أن يلي الفعل الفاعل، فيتوهم أن الداعي إلى الولي هو الفعل، والمقصود أنه الفاعل،",
     "en": "That is: the definite article is one of specific reference. He said “the rule is that it immediately follow the verb,” and did not say “that it follow it” — whereby the pronoun would refer to one of the two things, making it more concise and comprehensive — because of the obscurity of the more concise phrasing and its suggesting that the rule is that the verb should follow the agent, so that one might imagine that what calls for the following is the verb, whereas what is meant is that it is the agent [that should follow];"},
    {"type": "pair",
     "ar": "وللدلالة الاقتصار على ذكر الفعل على أن الشبه أولى بهذا الحكم؛ لأن الفعل مع قوة عمله إذا كان لا يرضى الفاعل بالفاصلة بينه وبين الفعل، فبالطريق الأولى ألا يرضى بالفصل بينه وبين ضعيف العمل.",
     "en": "and because confining the mention to the verb indicates that the [verb-]resembler is even more entitled to this ruling; for if the verb, despite the strength of its governance, does not tolerate that the agent be separated by an intervening element between it and the verb, then a fortiori it should not tolerate separation between it and a weak governor."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "حقيقة. ولا يخفى أن هذا التكلف مما يحتاج إليه أيضا في التعريف في قوله: «وقدم عليه»، وكأنه لم يتنبه له فأهمله أو حكما كما في الفاعل المستتر، فإن البعدية هنا حكمية كوجوده؛ إذ هو خلاف الأصل لمانع الاستتار.",
     "en": "…in reality. It is not hidden that this labored device is needed also in the definition, in his words “and is placed before it”; it seems he did not attend to it and so neglected it — or [the following is] in ruling only, as in the case of the concealed agent, for the “afterness” here is by ruling, like its existence, since it is contrary to the rule owing to the impediment of concealment."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "لأن النسبة إلى الفاعل مقوم لمدلول الفعل، وطرف النسبة الذي هو فاعل ههنا داخل في قوام النسبة إلى الفاعل ومقوم لها، ومقوم المقوم مقوم،",
     "en": "Because the relation to the agent is constitutive of the verb’s meaning, and the term of the relation which is the agent is here included in the constitution of the relation to the agent and is constitutive of it; and what constitutes the constituent is itself a constituent."},
    {"type": "pair",
     "ar": "فكما أن الهيئة لدلالتها على النسبة كانت جزءا للفعل كذلك الفاعل لدلالة على ما هو داخل في قوام النسبة كان في عداد جزئه.",
     "en": "So just as the [verbal] form, because it signifies the relation, was a part of the verb, likewise the agent, because it signifies what is included in the constitution of the relation, is to be counted among its parts."},
]
