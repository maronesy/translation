# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 441 (printed ٤٤٠)."""

PAGE_NUMBER = 441
PRINTED_PAGE = "٤٤٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «قلنا: جاز أن يجعل الأم مسماة باسم الأب … ثم يؤول» at the foot of PDF p. 440 (mid-sentence).
    {"type": "matn",
     "ar": "الاسم بمعنى المسمى به، ليحصل مفهوم يتناولهما، فيتجانسان، فيثنى باعتباره،",
     "en": "…the noun in the sense of “what is named by it”, so that a concept covering both is obtained; thus they become of one genus, and it is put in the dual with respect to that [concept];"},
    {"type": "matn",
     "ar": "فيكون معنى الأبوين «المسميين بالأب»، وكذلك الحال في الشمس بالنسبة إلى القمر.",
     "en": "so the meaning of “al-abawayn” is “the two named ‘father’”; and the same holds for the sun in relation to the moon."},
    {"type": "matn",
     "ar": "فإن قلت: فليعتبر مثل هذا التأويل في «القرء» أيضا بلا احتياج إلى ادعاء اسميته للطهر والحيض،",
     "en": "If you say: then let a like construal be considered for “al-qurʾ” too, with no need to claim that it names purity and menstruation,"},
    {"type": "matn",
     "ar": "فإنه موضوع لكل واحد منهما حقيقة، وليؤول بالمسمى به، ليحصل مفهوم يتناولهما، فيثنى باعتباره؟",
     "en": "since it is coined for each of them literally; and let it be construed as “what is named by it”, so that a concept covering both is obtained, and it is put in the dual with respect to that?"},
    {"type": "matn",
     "ar": "قلنا: لا شبهة في صحة[[١]] هذا الاعتبار لكن الكلام في جواز تثنيته بمجرد اشتراكه اللفظي بينهما،",
     "en": "We say: there is no doubt about the validity of this consideration; but the discussion concerns whether it may be put in the dual by the mere verbal equivocity (ishtirāk lafẓī) between the two,"},
    {"type": "matn",
     "ar": "وهو الذي اختلف فيه، والمصنف اختار عدم جوازه[[٢]]،",
     "en": "and that is what is disputed; the author chose that it is not allowed."},
    {"type": "matn",
     "ar": "وبهذا الاعتبار صح تثنية الأعلام المشتركة حقيقة أو ادعاء وجمعها،",
     "en": "By this consideration the dual and plural of proper names shared literally or by claim are valid."},
    {"type": "matn",
     "ar": "فـ«زيد» مثلا إذا كان علما لكثرة يؤول بـ«المسمى بزيد»، ثم يثنى ويجمع،",
     "en": "Thus “Zayd”, for example, when it is a proper name for many, is construed as “the one named Zayd”, then put in the dual and plural;"},
    {"type": "matn",
     "ar": "وكذا «عمر» إذا صار علما ادعائيا لأبي بكر يؤول بـ«المسمى بعمر» ثم يثنى ويجمع.",
     "en": "likewise “ʿUmar”, when it becomes a proper name for Abū Bakr by claim, is construed as “the one named ʿUmar”, then put in the dual and plural."},
    {"type": "matn",
     "ar": "ورده بعضهم وقال: الأولى أن يقال: الأعلام لكثرة استعمالها، وكون الخفة مطلوبة فيها يكفي لتثنيتها وجمعها مجرد الاشتراك في الاسم، بخلاف أسماء الأجناس،",
     "en": "Some rejected this and said: it is better to say that, for proper names, because of their frequent use and because lightness is sought in them, mere sharing in the name suffices for their dual and plural, unlike generic nouns (asmāʾ al-ajnās)."},
    {"type": "matn",
     "ar": "فعلى قول هذا البعض ينبغي ألا يذكر في تعريف التثنية قوله: «من جنسه».",
     "en": "On the view of these, his words “of its genus” ought not to be mentioned in the definition of the dual."},
    {"type": "matn",
     "ar": "ولما كان آخر الاسم المفرد الذي لحقه علامة التثنية في بعض المواد عما يتطرق إليه التغير أراد المصنف أن يبين حكم ما يتطرق إليه التغير؛",
     "en": "Since the end of the singular noun to which the sign of the dual is attached is, in some materials, among what is subject to change, the author wished to explain the rule of what is subject to change,"},
    {"type": "matn",
     "ar": "لأن حكم ما وراءه يعلم من تعريف المثنى، فقال:",
     "en": "because the rule of what lies beyond it is known from the definition of the dual. So he said:"},
    {"type": "matn",
     "ar": "(فالمقصور) أي: الاسم المقصور[[٣]]، وهو: «ما في آخره ألف مفردة[[٤]] لازمة[[٥]]»،",
     "en": "(The shortened noun (maqṣūr)), that is, the shortened noun, which is “that at whose end there is a single, necessary alif”."},
    {"type": "matn",
     "ar": "ويسمى مقصورا؛ لأنه ضد الممدود[[٦]]، أو لأنه محبوس من",
     "en": "It is called “maqṣūr” because it is the opposite of the lengthened (mamdūd), or because it is withheld from…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لأن هذا استعمال اللفظ في المعنى المجازي، ولا نزاع في تثنية اللفظ باعتبار المعنى المجازي.",
     "en": "Because this is the use of the word in a figurative sense, and there is no dispute about putting a word in the dual with respect to a figurative sense."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: في شرح الكافية. وفي الإيضاح جوزه شاذا. لذا قال الشارح: والمصنف متردد في ذلك.",
     "en": "That is, in Sharḥ al-Kāfiya. In al-Īḍāḥ he allowed it as irregular. Hence the commentator said: the author is hesitant about this."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أشار بتقدير الاسم إلى أن المقصور في الاصطلاح لا يكون إلا اسما، فلا يقال: رمى مقصور.",
     "en": "By supplying “noun” he indicated that the maqṣūr in technical usage is only a noun; so one does not say that “ramā” (he threw) is maqṣūr."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "احترز بقوله: مفردة عن المقرونة بهمزة، فإنها ممدودة",
     "en": "By his word “single” he excludes the alif joined to a hamza, for that is lengthened (mamdūda);"},
    # REVIEW: printed «مقصودا»; the sense requires «مقصورا» (maqṣūr). Transcribed as printed, translated as maqṣūr.
    {"type": "pair",
     "ar": "بقوله: لازمة عن الألف زائدة في الوقف، فإنها لا يصير زائدا بها مقصودا لعدم لزومها لاختصاصها بحال الوقف.",
     "en": "and by his word “necessary” the alif added in pause, for “Zaydā” does not become maqṣūr by it, since it is not necessary, being specific to the state of pause."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: في الاصطلاح نقل عنه أن قوله: مفردة احتراز عن الألف المقرونة بهمزة كحمراء، وقوله: لازمة احتراز عن مثل: زيد إلى آخره إذا وقفت عليه.",
     "en": "That is, in technical usage. It is reported from him that his word “single” excludes the alif joined to a hamza, as in “ḥamrāʾ”, and his word “necessary” excludes the like of “Zayd” [in the accusative] and so on, when you pause on it."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "يعني أخذ من القصر بمعنى خلاف المد، والتوجيه الآخر بالنظر إلى أخذه من القصر بمعنى الحبس،",
     "en": "He means: it is taken from qaṣr in the sense of the opposite of extension (madd); the other explanation regards it as taken from qaṣr in the sense of withholding."},
    {"type": "pair",
     "ar": "ولك أن تجعله من القصر كعنب بمعنى خلاف الطول، فإن الممدود طويل بالنسبة إلى المقصور،",
     "en": "You may also derive it from qiṣar, on the pattern of ʿinab, in the sense of the opposite of length, for the mamdūd is long relative to the maqṣūr."},
    {"type": "pair",
     "ar": "يقال: قصر ككرم، فهو قصير وقصره كضربه جعله قصيرا كل ذلك من القاموس.",
     "en": "One says “qaṣura”, like “karuma”, so it is “qaṣīr” (short); and “qaṣarahu”, like “ḍarabahu”, means he made it short. All of this is from al-Qāmūs."},
]
