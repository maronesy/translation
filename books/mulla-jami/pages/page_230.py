# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 230 (printed ٢٢٩)."""

PAGE_NUMBER = 230
PRINTED_PAGE = "٢٢٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "بشرط ألا يكون الفعل المشتغل عنه طلبا كالأمر والنهي والدعاء[[١]] نحو: «لقيت القوم، وأما زيد فأكرمته»،",
     "en": "…on condition that the verb diverted from it is not a request, such as a command, a prohibition or a supplication, as in “I met the people; as for Zayd, I honoured him” (laqītu al-qawma wa-ammā Zaydun fa-akramtuhu)."},
    {"type": "matn",
     "ar": "فالعطف على الفعلية قرينة للنصب، وكلمة «أما» قرينة للرفع، وهي أقوى؛ لأنها لا يقع بعدها غالبا إلا المبتدأ،",
     "en": "Coordination with the verbal sentence is an indication for the accusative, and the word “ammā” is an indication for the nominative, and it is stronger; because after it, as a rule, only a mubtadaʾ occurs,"},
    {"type": "matn",
     "ar": "بخلاف عطف الاسمية على الفعلية، فإنه كثير الوقوع في كلامهم مع أنها تأيدت بالسلامة عن الحذف أيضا،",
     "en": "unlike the coordination of a nominal sentence with a verbal one, which occurs frequently in their speech; and moreover it is supported by freedom from elision as well."},
    {"type": "matn",
     "ar": "وإنما قال مع غير الطلب احترازا عما إذا كانت مع الطلب نحو: «أما زيدا فاضربه»؛ فإن المختار حينئذ هو النصب،",
     "en": "He said “with something other than a request” only to exclude the case where it is with a request, as in “As for Zayd, strike him” (ammā Zaydan fa-ḍribhu); for then the accusative is preferred,"},
    {"type": "matn",
     "ar": "فإن الرفع يقتضي[[٢]] وقوع الطلب خبرا، وهو لا يجوز إلا بتأويل.",
     "en": "since the nominative requires the request to occur as a khabar, which is not allowed except by interpretation."},
    {"type": "matn",
     "ar": "(و) مثل «أما» مع غير الطلب («إذا») الواقع على الاسم المذكور (للمفاجأة) في كونه من أقوى قرائن الرفع مثل: «خرجت فإذا زيد يضربه عمرو»، فإن المختار فيه الرفع،",
     "en": "(And) like “ammā” with something other than a request, in being among the strongest indications for the nominative, is (“idhā”) occurring before the noun mentioned (of surprise—li-l-mufājaʾa), as in “I went out, and behold, Zayd—ʿAmr is striking him” (kharajtu fa-idhā Zaydun yaḍribuhu ʿAmrun); for the nominative is preferred in it,"},
    {"type": "matn",
     "ar": "فإن «إذا» للمفاجأة لا تدخل إلا على الجملة الاسمية غالبا،",
     "en": "since “idhā” of surprise, as a rule, enters only on a nominal sentence."},
    {"type": "matn",
     "ar": "وما وقع في بحث الظروف من أن «إذا» المفاجأة يلزم بعدها الاسمية، فالمراد بلزوم الاسمية[[٣]] غلبة وقوعها بعدها، فلا تناقض.",
     "en": "As for what occurs in the discussion of adverbs (ẓurūf)—that after “idhā” of surprise a nominal sentence is necessary—what is meant by “necessary” is that it predominantly occurs after it; so there is no contradiction."},
    {"type": "matn",
     "ar": "(ويختار النصب) في الاسم المذكور (بالعطف[[٤]]) أي: بسبب عطف جملة هو فيها (على جملة فعلية) متقدمة (للتناسب) أي: لرعاية التناسب بين الجملة المعطوفة",
     "en": "(And the accusative is preferred) in the noun mentioned (through coordination), that is, because of the coordination of a sentence in which it stands (with a verbal sentence) that precedes, (for the sake of correspondence—li-l-tanāsub), that is, to observe correspondence between the coordinated sentence…"},

    {"type": "rule"},

    # ---------------- Footnote 8 of the previous page, continued ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "فقد أكرمته» في جواب «أيهم أكرمت»؛ لأن القرينة التي تقوى جانب النصب، هي التناسب والتطابق المذكوران.",
     "en": "…I have honoured him,” in answer to “Which of them did you honour?”; because the indication that strengthens the side of the accusative is the correspondence and agreement mentioned."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وخص الطلب بها؛ لأنها إذا كانت مع غيرها كالاستفهام مثلا لم يكن من هذا الباب لامتناع التسليط على الاسم.",
     "en": "He restricted the request to these, because if it were with something else, such as an interrogative for example, it would not belong to this chapter, since bringing [the verb] to bear on the noun is then impossible."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أو إن الجملة الطلبية قلما تكون اسمية لاختصاص الطلب بالفعل.",
     "en": "Or because a requestive sentence is seldom nominal, since request is proper to the verb."},
    {"type": "pair",
     "ar": "ألا ترى إلى اقتضاء حروف الطلب للفعل كحروف الاستفهام والعرض والتحضيض، ولا يعارضه السلامة عن الحذف لكثرة وقوعه في كلامهم.",
     "en": "Do you not see that the particles of request require the verb, such as the particles of interrogation, of proposal (ʿarḍ) and of urging (taḥḍīḍ)? Freedom from elision does not oppose this, because of how frequently it occurs in their speech."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "والمراد لزوم الاسمية في غير هذا الموضع لورود النصب ههنا.",
     "en": "What is meant is the necessity of the nominal sentence outside this place, since the accusative is attested here."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    # REVIEW: print reads «علة جملة»; the lemma in the matn is «على جملة»; transcribed as printed.
    {"type": "pair",
     "ar": "علة جملة فعلية حقيقة أو حكما، نحو: مررت برجل ضارب عمرا وهندا يقتلها، فإن اسم الفاعل لشبهه بالفعل في حكمه.",
     "en": "[With] a verbal sentence, really or by legal status, as in “I passed by a man striking ʿAmr, and Hind—he is killing her”; for the active participle, owing to its resemblance to the verb, has its status."},
    {"type": "pair",
     "ar": "واستثنى سيبويه عن الجملة الفعلية الجملة التعجبية نحو: «أحسن بزيد وعمرو يضربه»، لكون فعل التعجب لجموده وتجرده عن العروض لاحقا بالأسماء،",
     "en": "Sībawayh excepted from the verbal sentence the sentence of wonder (taʿajjub), as in “How fine is Zayd! And ʿAmr—he strikes him” (aḥsin bi-Zaydin wa-ʿAmrun yaḍribuhu), because the verb of wonder, owing to its fixity and its being free of accidents, is joined to the nouns."},
    {"type": "pair",
     "ar": "يقال: والظاهر أن الجملة الثانية في المثال المفروض اعتراضية لا عاطفة، وإلا لزم عطف الخبرية على الإنشائية،",
     "en": "It is said: what is apparent is that the second sentence in the supposed example is parenthetical (iʿtirāḍiyya), not coordinated; otherwise there would follow the coordination of an informative sentence with a performative (inshāʾiyya) one."},
    {"type": "pair",
     "ar": "وفيه أن «عمرو يضربه» استعمل في إنشاء التحزن والتحسر.",
     "en": "Against this: “ʿAmrun yaḍribuhu” is used to perform [an expression of] grief and regret."},
    # REVIEW: print reads «قال زيد عمر وقائم»; probably «عمرو قائم» with the wāw misplaced; transcribed as printed.
    {"type": "pair",
     "ar": "ومما أظنه أنه ينبغي أن يستثنى ما إذا كانت الجملتان مقولي القول نحو: «قال زيد عمر وقائم وبكرا ضربته»،",
     "en": "Among what I think is that one should except the case where the two sentences are both objects of saying, as in “Zayd said: ʿAmr is standing, and Bakr—I struck him”;"},
    {"type": "pair",
     "ar": "فإنه ليس العطف في مقولي القول باعتبار اشتراكهما في التحقيق حتى يتفاوت الاسمية والفعلية في التناسب باعتبار أنهما مقولان، ولا تفاوت في المقولية بين الإنشاء.",
     "en": "for coordination between two objects of saying is not with respect to their sharing in actual realization, such that nominal and verbal would differ in correspondence; [it is] with respect to their being things said, and there is no difference in being said among performatives."},
]
