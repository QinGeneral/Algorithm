/*
 * @lc app=leetcode.cn id=1114 lang=java
 *
 * [1114] 按序打印
 */

// @lc code=start
class Foo {

    private volatile boolean isFirstInvoked = false;
    private volatile boolean isSecondInvoked = false;

    public Foo() {

    }

    public void first(Runnable printFirst) throws InterruptedException {

        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        isFirstInvoked = true;
    }

    public void second(Runnable printSecond) throws InterruptedException {
        while (!isFirstInvoked) {
            Thread.sleep(10);
        }
        // printSecond.run() outputs "second". Do not change or remove this line.
        printSecond.run();
        isSecondInvoked = true;
    }

    public void third(Runnable printThird) throws InterruptedException {
        while (!isSecondInvoked) {
            Thread.sleep(10);
        }
        // printThird.run() outputs "third". Do not change or remove this line.
        printThird.run();
    }
}
// @lc code=end
