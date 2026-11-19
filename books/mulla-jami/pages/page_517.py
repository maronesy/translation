# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 517 (printed ٥١٦)."""

PAGE_NUMBER = 517
PRINTED_PAGE = "٥١٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «ومعنى «أبصرت» قريب من» at the foot of PDF p. 516 (mid-sentence).
    {"type": "quran",
     "ar": "معنى «علمت» بالحاسة، ومنه قوله تعالى: ﴿فانظر ماذا ترى﴾[[١]]",
     "en": "…the meaning of “ʿalimtu” through the sense faculty; from it is His words, the Exalted: “So consider what you see [i.e., think]” (Qurʾān, Sūrat al-Ṣāffāt 37:102);"},
    {"type": "matn",
     "ar": "(و«وجدت» بمعنى: «أصبت») تقول: وجدت الضالة أي: أصبتها وعلمتها بالحاسة،",
     "en": "(and “wajadtu” in the sense of “aṣabtu” (I came upon)): you say “wajadtu al-ḍāllata” (I found the stray), that is, I came upon it and knew it through the senses."},
    {"type": "matn",
     "ar": "ولما كان مراده أن لها معان أخر قريبة من معنى العلم والظن، لم يتعرض لـ«علم» بمعنى: صار مشقوق الشفة العليا،",
     "en": "Since what he meant is that they have other meanings close to the meaning of knowledge and supposition, he did not deal with “ʿalima” in the sense of “he became split in the upper lip”,"},
    {"type": "matn",
     "ar": "ولـ«وجدت جدة» و«وجدت موجدة» و«وجدت وجدا» أي: استغنيت وغضبت وحزنت؛ لأنها ليست بمعنى العلم والظن.",
     "en": "nor with “wajadtu jidatan”, “wajadtu mawjidatan” and “wajadtu wajdan”, that is, I became rich, I became angry and I grieved; for these are not in the sense of knowledge and supposition."},

    {"type": "section", "ar": "[الأفعال الناقصة]",
     "en": "The Defective Verbs (al-Afʿāl al-Nāqiṣa)"},

    {"type": "matn",
     "ar": "(الأفعال الناقصة) إنما سميت ناقصة؛ لأنها لا يتم بمرفوعها[[٢]] كالأفعال الغير الناقصة",
     "en": "(The defective verbs (al-afʿāl al-nāqiṣa)) are called defective only because they are not complete with their nominative, unlike the non-defective verbs."},
    {"type": "matn",
     "ar": "(ما وضع) أي: أفعال وضعت (لتقرير الفاعل على صفة) أي: العمدة فيما وضعت له هذه الأفعال هو تقرير الفاعل[[٣]] على صفة،",
     "en": "(They are what was assigned), that is, verbs that were assigned, (for establishing the agent in an attribute), that is, the principal element in what these verbs were assigned for is the establishing of the agent in an attribute;"},
    {"type": "matn",
     "ar": "ولا شك أن هذه الصفة خارجة عن ذلك التقرير الذي هو العمدة في الموضوع له؛",
     "en": "and there is no doubt that this attribute lies outside that establishing which is the principal element in what [the verb] was assigned for,"},
    {"type": "matn",
     "ar": "لأن ذلك التقرير[[٤]] نسبة بين الفاعل والصفة، فكل من طرفيها خارج عنها،",
     "en": "because that establishing is a relation between the agent and the attribute, and each of its two terms lies outside it."},
    {"type": "matn",
     "ar": "فخرج عن الحد الأفعال التامة؛ لأنها موضوعة لصفة[[٥]] وتقرير الفاعل عليها،",
     "en": "So the complete verbs are excluded from the definition, since they are assigned for an attribute together with the establishing of the agent in it;"},
    {"type": "matn",
     "ar": "فكل من الصفة[[٦]] والتقرير عمدة فيما وضعت له لا التقرير وحده،",
     "en": "so both the attribute and the establishing are principal elements in what they were assigned for, not the establishing alone."},
    {"type": "matn",
     "ar": "وإنما جعلنا التقرير المذكور عمدة الموضوع له في الأفعال الناقصة لا تمامه لاشتمالها على معان زائدة على ذلك التقرير كالزمان في الكل والانتقال والدوام",
     "en": "We made the establishing mentioned the principal element of what the defective verbs were assigned for, not the whole of it, only because they include meanings in addition to that establishing, such as time in all of them, and transition and permanence…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سورة الصافات: ١٠٢.",
     "en": "Sūrat al-Ṣāffāt 37:102."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وقيل: لنقصان مدلولها عن مدلول التامة بالحدث الداخل في التامة دونها.",
     "en": "It has been said: because what they signify falls short of what the complete [verbs] signify, by the event (ḥadath), which enters into the complete [verbs] but not into them."},
    {"type": "pair",
     "ar": "وفيه نظر لأنهم لا يسمون أفعال المدح والذم ناقصة مع نقصان مدلولها عن غيرها بالزمان.",
     "en": "This is open to question, because they do not call the verbs of praise and blame defective, although what they signify falls short of [that of] other [verbs] by time."},
    {"type": "pair",
     "ar": "ولك أن تقول: سميت بها لنقصان عددها بالنسبة إلى الأفعال التي تتم بمرفوعها، وفيه ما فيه.",
     "en": "You may say: they were so named because of their small number in relation to the verbs that are complete with their nominative; but this has what it has [i.e., is weak]."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "اعلم أن مدلول «كان» نسبة الصفة إلى فاعله، والزمان والنسبة هي ثبوت الصفة للفاعل،",
     "en": "Know that what “kāna” signifies is the relation of the attribute to its agent, and time; and the relation is the attribute’s being established for the agent."},
    {"type": "pair",
     "ar": "وفرق بينها، وبين التقرير الذي هو صفة المتكلم إن كان مصدرا مبنيا للفاعل كما هو الظاهر، وبين التقرير الذي هو صفة الفاعل إن كان مبنيا للمفعول،",
     "en": "There is a difference between it and the establishing that is an attribute of the speaker, if [taqrīr] is a verbal noun of the active voice, as is apparent, and the establishing that is an attribute of the agent, if it is of the passive voice;"},
    {"type": "pair",
     "ar": "فإرادة ثبوت الصفة للفاعل مسامحة لا تليق بمقام التعريف.",
     "en": "so to mean [by taqrīr] the establishment of the attribute for the agent is a laxity unbefitting the context of definition."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: التقرير المقيد، والتقييد لا يخرجه عن كونه نسبة بين الفاعل والصفة، كما توهم.",
     "en": "That is, the qualified establishing; and the qualification does not take it out of being a relation between the agent and the attribute, as has been imagined."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "يعني: الحدث والنسبة إلى الفاعل المعين، ولم يتعرض للزمان لاشتراكه في التامة والناقصة.",
     "en": "He means: the event and the relation to the specific agent; he did not deal with time because it is shared by the complete and the defective [verbs]."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "يعني: كلاهما مستويان بالنظر إلى الموضوع له ليس لأحدهما مزية على الآخر بحيث يمكن أن يقال: إنه الموضوع له",
     "en": "He means: both are equal with regard to what [the verb] is assigned for; neither has a superiority over the other such that it could be said “it is what [the verb] is assigned for”;"},
    {"type": "pair",
     "ar": "فلا يصدق على الأفعال التامة أنها وضعت للتقرير باعتبار أنه عمدة بالقياس إلى الحدث والزمان،",
     "en": "so it is not true of the complete verbs that they were assigned for the establishing, on the view that it is the principal element in comparison with the event and time."},
    {"type": "pair",
     "ar": "فلا يرد ما قيل: إنه إذا كان كل منهما عمدة فيها يصدق أن التقرير عمدة فيما وضعت له، فلا يخرج عن التعريف إلا أن يعتبر قيد فقط، واللفظ لا يساعده.",
     "en": "So the objection does not hold that, if each of them is a principal element in them, it is true that the establishing is a principal element in what they were assigned for, and so they are not excluded from the definition unless the qualification “only” is taken into account, which the wording does not support."},
]
