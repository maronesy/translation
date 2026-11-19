# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 236 (printed ٢٣٥)."""

PAGE_NUMBER = 236
PRINTED_PAGE = "٢٣٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «لكون الألف واللام» from the foot of PDF p. 235.
    {"type": "matn",
     "ar": "في «الزانية والزاني» مبتدأ موصولا فيه معنى الشرط، واسم الفاعل الذي هو صلته كالشرط، فخبر المبتدأ كالجزاء،",
     "en": "…in “al-zāniyatu wa-l-zānī” being a relative mubtadaʾ containing the sense of the condition; the active participle (ism al-fāʿil) that is its relative clause (ṣila) is like the condition, and so the khabar of the mubtadaʾ is like the apodosis (jazāʾ);"},
    {"type": "matn",
     "ar": "والفاء الداخلة عليه مرتبطة بالشرط؛ لدلالته على سببيته للجزاء،",
     "en": "and the fāʾ that enters upon it is linked to the condition, because it indicates that [the condition] is the cause of the apodosis."},
    {"type": "matn",
     "ar": "ومثل هذا الفاء[[١]] لا يعمل ما في حيزه في ما قبله، فامتنع تسليط الفعل المذكور بعده على ما قبله، فتعين فيه الرفع.",
     "en": "What lies within the scope of a fāʾ like this does not govern what precedes it; so it is excluded that the verb mentioned after it be brought to bear on what precedes it, and the nominative is required in it."},
    {"type": "matn",
     "ar": "(و) الآية (جملتان) مستقلتان (عند سيبويه) إذ «الزانية»[[٢]] مبتدأ محذوف المضاف[[٣]]، و«الزاني» عطف عليه، والخبر محذوف،",
     "en": "(And) the verse is (two) independent (sentences according to Sībawayh), since “al-zāniya” is a mubtadaʾ whose annexing noun (muḍāf) is elided, “al-zānī” is conjoined to it, and the khabar is elided;"},
    {"type": "matn",
     "ar": "أي: حكم الزانية والزاني فيما يتلى عليكم بعد،",
     "en": "that is: “the ruling on the adulteress and the adulterer is in what will be recited to you hereafter.”"},
    {"type": "matn",
     "ar": "وقوله: «فاجلدوا» جملة ثانية لبيان الحكم الموعود، والفاء عنده أيضا للسببية، أي: إن ثبت زناهما[[٤]] فاجلدوا.",
     "en": "His words “fa-jlidū” (so flog) are a second sentence, explaining the promised ruling; and the fāʾ is, in his view too, causal, that is: “if their fornication is established, then flog.”"},
    {"type": "matn",
     "ar": "وقيل: زائدة[[٥]] أو للتفسير[[٦]]، وجزء الجملة[[٧]] لا يعمل في جزء جملة أخرى، فيمتنع التسليط، فلا يدخل في الضابطة، فتعين الرفع.",
     "en": "It has been said: [the fāʾ] is redundant, or explanatory; and a part of one sentence does not govern a part of another sentence, so bringing [the verb] to bear is excluded; hence it does not fall under the rule, and the nominative is required."},
    # REVIEW: print reads «فهي يكون» (masculine verb after feminine pronoun); transcribed as printed.
    {"type": "matn",
     "ar": "(وإلا) أي: وإن لم يكن الفاء فمعنى الشرط، ولم تكن الآية جملتين أيضا، فهي يكون داخلة تحت الضابطة",
     "en": "(Otherwise), that is: if the fāʾ is not in the sense of the condition, and the verse is not two sentences either, then it falls under the rule,"},
    {"type": "matn",
     "ar": "(فالمختار) حينئذ فيها (النصب) واختيار النصب[[٨]] باطل؛ لاتفاق القراء على الرفع،",
     "en": "(and the preferred [case]) in it would then be (the accusative); but preferring the accusative is invalid, because the readers agreed on the nominative."},
    {"type": "matn",
     "ar": "فلا بد من جعل الفاء بمعنى الشرط أو جعل الآية جملتين، لتعين الرفع.",
     "en": "So one must take the fāʾ in the sense of the condition or take the verse as two sentences, so that the nominative is required."},

    {"type": "rule"},

    # ---------------- Footnote 9 of p. 235, continued ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "عمران: ١٩).",
     "en": "…ʿImrān 3:19)."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "إنما قال: مثل لأن الفاء إذا كانت زائدة أو غير واقعة موقعها لغرض كما في قوله تعالى: ﴿فأما اليتيم فلا تقهر﴾ (سورة الضحى: ٩)، جاز أن يعمل ما بعدها فيما قبلها.",
     "en": "He said “like [this]” only because, when the fāʾ is redundant, or not in its proper place for some purpose, as in His words, the Exalted: “As for the orphan, do not oppress [him]” (Qurʾān, Sūrat al-Ḍuḥā 93:9), what follows it may govern what precedes it."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "توجيه المبرد أقوى من هذا التوجيه لعدم احتياجه إلى إضمار. ولذا قدمه المصنف،",
     "en": "Al-Mubarrad’s explanation is stronger than this explanation, since it needs no suppression (iḍmār); for this reason the author put it first."},
    {"type": "pair",
     "ar": "لكن فيه أنه يلزم أن يكون الإنشاء خبرا.",
     "en": "Against it, however, is that it entails a performative utterance (inshāʾ) being a khabar."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أو خبر كذلك. والتقدير: هذا حكم الزانية والزاني، كما يقال في المفصل واللباب.",
     "en": "Or a khabar likewise [with the annexing noun elided]; the implied form being: “This is the ruling on the adulteress and the adulterer,” as is said in al-Mufaṣṣal and al-Lubāb."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "شرعا. وذلك بأربعة شهداء أو بالإقرار.",
     "en": "[Established] legally; that is, by four witnesses or by confession."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وما بعدها ابتداء كلام. ولا يخفى أن القول بالزيادة مع ظهور احتمال السبب بعيد.",
     "en": "And what follows it begins a new utterance. It is not hidden that holding it redundant, when the possibility of causality is evident, is far-fetched."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لأن «اجلدوا» إيجاب، والإيجاب متضمن للوجوب الذي هو الحكم.",
     "en": "Because “ijlidū” (flog) is an imposing of obligation (ījāb), and imposing obligation includes the obligatoriness (wujūb) that is the ruling."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "يجوز أن يقال: إن ما بعد فاء التفسير أو السببية إذا كانت الفاء واقعة موقعها لا تعمل فيما قبلها.",
     "en": "It may be said: what follows an explanatory or causal fāʾ, when the fāʾ is in its proper place, does not govern what precedes it."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "يعني: أن الشرطية إشارة إلى قياس استثنائي استثنى فيه نقيض التالي ليثبت نقيض المقدم.",
     "en": "He means: the conditional [sentence] points to an exceptive (conditional) syllogism (qiyās istithnāʾī) in which the contradictory of the consequent is affirmed in order to establish the contradictory of the antecedent."},
    {"type": "pair",
     "ar": "وهو ما ذهب إليه المبرد وسيبويه.",
     "en": "This is what al-Mubarrad and Sībawayh held."},
    {"type": "pair",
     "ar": "وإنما حمله على ذلك إذ لو لم يحمله لكان معناه أن اختيار النصب واقع على بعض التقادير، لكنه غير واقع أصلا، فإن الشاذ لا يعبأ به.",
     "en": "He took it thus only because, had he not done so, its meaning would be that preferring the accusative does occur on some construals; but it does not occur at all, for the anomalous [reading] is disregarded."},
]
