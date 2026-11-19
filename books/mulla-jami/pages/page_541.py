# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 541 (printed ٥٤٠)."""

PAGE_NUMBER = 541
PRINTED_PAGE = "٥٤٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «أو من الزمان، نحو: «صمت» at the foot of PDF p. 540 (mid-sentence).
    {"type": "matn",
     "ar": "من يوم الجمعة».",
     "en": "…from Friday”."},
    {"type": "matn",
     "ar": "وعلامة «من» الابتدائية صحة إيراد «إلى» أو «ما يفيد فائدتها» في مقابلتها نحو: «سرت من البصرة إلى الكوفة»،",
     "en": "The sign of the min of beginning is that “ilā”, or “what gives its sense”, can validly be set against it, as in “I travelled from Baṣra to Kūfa”,"},
    {"type": "matn",
     "ar": "ونحو: «أعوذ بالله من الشيطان الرجيم»؛ لأن معنى أعوذ به: ألتجئ إليه.",
     "en": "and as in “I seek refuge in Allah from the accursed Satan”, because the meaning of “aʿūdhu bihi” is “I take shelter with Him”."},
    {"type": "matn",
     "ar": "٢-(والتبيين) بالجر عطفا على «الابتداء»[[١]]، أي: ويجيء «من» للتبيين أيضا؛ أي: لإظهار المقصود من أمر مبهم.",
     "en": "2. (And explication (tabyīn)), in the genitive, coordinated with “al-ibtidāʾ”; that is, “min” also comes for explication, that is, for making clear what is intended by something vague."},
    {"type": "matn",
     "ar": "وعلامته: صحة وضع الموصول في موضعه[[٢]]، مثل: ﴿فاجتنبوا الرجس من الأوثان﴾[[٣]]،",
     "en": "Its sign is that a relative can validly be put in its place, as in “So shun the filth of idols”;"},
    {"type": "matn",
     "ar": "فإنك لو قلت: «فاجتنبوا الرجس الذي هو الأوثان» استقام المعنى.",
     "en": "for if you said “so shun the filth which is the idols”, the meaning would be sound."},
    {"type": "matn",
     "ar": "٣-(والتبعيض) أي: وقد يجيء[[٤]] «من» للتبعيض.",
     "en": "3. (And partition (tabʿīḍ)); that is, “min” sometimes comes for partition."},
    {"type": "matn",
     "ar": "وعلامة صحة وضع «بعض» مكانه نحو: «أخذت من الدراهم» أي: بعض الدراهم.",
     "en": "Its sign is that “baʿḍ” (some) can validly be put in its place, as in “I took of the dirhams”, that is, some of the dirhams."},
    {"type": "matn",
     "ar": "٤-(وزائدة) عطف على قوله: «للابتداء»، فإنه مرفوع بالخبرية.",
     "en": "4. (And redundant (zāʾida)), coordinated with his words “li-l-ibtidāʾ”, for that is in the nominative as a predicate."},
    {"type": "matn",
     "ar": "وزيادتها لا يكون إلا (في غير) الكلام (الموجب) نحو: «ما جاءني من أحد»[[٥]]، و«هل جاءك من أحد؟» و«لا تضرب من أحد».",
     "en": "Its being redundant occurs only (in non-affirmative) speech, as in “mā jāʾanī min aḥadin” (no one at all came to me), “hal jāʾaka min aḥadin?” (did anyone at all come to you?) and “lā taḍrib min aḥadin” (do not strike anyone at all)."},
    {"type": "matn",
     "ar": "(خلافا للكوفيين والأخفش)، فإنهم يجوزون زيادتها في الموجب أيضا مستدلين بقولهم: «قد كان من مطر».",
     "en": "(Contrary to the Kūfans and al-Akhfash), for they allow its being redundant in affirmative speech too, adducing as evidence the Arabs’ saying “qad kāna min maṭarin” (there has been rain)."},
    {"type": "matn",
     "ar": "فأجاب عن استدلالهم بقوله: («وقد كان من مطر» وشبهه) مما يتوهم منه زيادة «من» في الكلام الموجب (متأول) بكونها للتبعيض أو التبيين أي: «وقد كان بعض",
     "en": "So he answered their argument with his words: (“wa-qad kāna min maṭarin” and the like), in which “min” might be thought redundant in affirmative speech, (is interpreted), as being for partition or explication, that is, “there has been some…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أشار بذلك إلى أن ما وقع في بعض النسخ وللتبيين بإعادة الجار غلط؛",
     "en": "By this he indicated that what occurs in some copies, “wa-li-l-tabyīn” with the preposition repeated, is an error,"},
    {"type": "pair",
     "ar": "إذ لا معنى لإعادة الجار هاهنا، وتركه في قوله: للتبعيض.",
     "en": "since there is no point in repeating the preposition here and omitting it in his words “li-l-tabʿīḍ”."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لا يقال: لا يصح وضع الموصول موضع «من» في «قد كان من مطر» أي: شيء من مطر مع أنه جعل «من» بيانية؛",
     "en": "It should not be said: a relative cannot validly be put in place of “min” in “qad kāna min maṭarin”, that is, “something of rain”, although he made “min” explicative,"},
    {"type": "pair",
     "ar": "لأنه يلزم وصف النكرة بالمعرفة، ويلزم جعل المفرد أي: مطر صلة؛",
     "en": "because it would entail qualifying an indefinite by a definite, and would entail making a single term, namely “maṭar”, a relative clause;"},
    {"type": "pair",
     "ar": "لأنا نقول: المراد وضع الموصول موضعه مع إيراد مقتضيات الموصول.",
     "en": "for we say: what is meant is putting the relative in its place together with supplying what the relative requires."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "سورة الحج: ٣٠.",
     "en": "Qurʾān, Sūrat al-Ḥajj 22:30."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أشار إلى أن مجيئه للتبعيض قليل بالنسبة إلى المعنيين السابقين، وإلى أنه يجوز أن يكون موضوعا له،",
     "en": "He indicated that its coming for partition is rare relative to the two preceding meanings, and that it may be coined for it,"},
    {"type": "pair",
     "ar": "وأن يكون راجعا إلى الابتداء، كما ذهب إليه المبرد وعبد القاهر والزمخشري؛ لأن الدراهم في قولك: «أخذت من الدراهم» مبدأ الأخذ.",
     "en": "or may reduce to beginning, as al-Mubarrad, ʿAbd al-Qāhir and al-Zamakhsharī held, because the dirhams in your saying “I took of the dirhams” are the starting point of the taking."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "والدليل على زيادتها دخولها على ما يوصل الفعل إليه، أعني: الفاعل،",
     "en": "The proof of its being redundant is its entering upon that to which the verb is made to reach [directly], namely the agent;"},
    {"type": "pair",
     "ar": "وأورد مثال النفي لأصالته والنهي والاستفهام شبهه.",
     "en": "he gave the example of negation because it is the principal case, and of prohibition and interrogation because they resemble it."},
    {"type": "pair",
     "ar": "وأورد مثال الاستفهام إشارة إلى اختصاص الحكم ب\"هل\".",
     "en": "He gave the example of interrogation to indicate that the rule is restricted to “hal”."},
]
